import hashlib
import json
import subprocess
import urllib.request
from pathlib import Path

root = Path('.')
record = '020'
prod = root / f'audio/production/record-{record}'
source_path = root / f'manuscript/records/{record}/current.md'
routing_path = root / f'audio/routing/record-{record}.json'
route_path = prod / 'route-plan.json'
subprocess.run(['python', 'scripts/audio_route.py', str(source_path), str(routing_path), str(route_path)], check=True)

captures = json.loads((prod / 'captures.json').read_text(encoding='utf-8'))
plan = json.loads(route_path.read_text(encoding='utf-8'))
source_hash = hashlib.sha256(source_path.read_bytes()).hexdigest()
assert source_hash == 'c6b10e568d9ebeeef68539c59c899ae340af7f581ab54a6d625e79857b1c826f'
assert plan['record'] == record
assert plan['routing_mode'] == 'exact_quote_locked'
assert plan.get('uses_timestamps_for_speaker_assignment') is False
assert plan['source_sha256'] == source_hash
assert captures['source_sha256'] == source_hash
assert captures['routing_mode'] == 'exact_quote_locked'
assert captures['status'] == 'candidate_unlistened'
assert ''.join(s['transcript'] for s in plan['segments']) == plan['audio_body']
assert len(plan['segments']) == len(captures['segments']) == 35
assert any(s['speaker'] == 'ithar' for s in plan['segments'])
for routed, captured in zip(plan['segments'], captures['segments']):
    assert routed['index'] == captured['index']
    assert int(routed['pause_after_ms']) == int(captured['pause_after_ms'])
    if routed['speaker'] == 'greg':
        assert routed['voice_id'] == 'deep'
    elif routed['speaker'] == 'ithar':
        assert routed['voice_id'] == 'normal'
    else:
        raise AssertionError(routed['speaker'])
for current, nxt in zip(plan['segments'], plan['segments'][1:]):
    if current['speaker'] != nxt['speaker']:
        assert int(current['pause_after_ms']) >= 1100

work = Path('/tmp/record-020-v2')
work.mkdir(parents=True, exist_ok=True)
concat = []
for item in captures['segments']:
    i = item['index']
    mp3 = work / f'{i:03d}.mp3'
    wav = work / f'{i:03d}.wav'
    urllib.request.urlretrieve(item['preview_url'], mp3)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', str(mp3), '-ar', '24000', '-ac', '1', '-c:a', 'pcm_s16le', str(wav)], check=True)
    concat.append(wav)
    ms = int(item['pause_after_ms'])
    if ms:
        silence = work / f'{i:03d}-silence.wav'
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'lavfi', '-i', 'anullsrc=r=24000:cl=mono', '-t', f'{ms / 1000:.3f}', '-c:a', 'pcm_s16le', str(silence)], check=True)
        concat.append(silence)

list_file = work / 'concat.txt'
list_file.write_text(''.join(f"file '{p}'\n" for p in concat), encoding='utf-8')
asset = 'audio/assets/record-020-quote-locked-v2.mp3'
out = root / asset
out.parent.mkdir(parents=True, exist_ok=True)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', str(list_file), '-c:a', 'libmp3lame', '-b:a', '128k', str(out)], check=True)
duration = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', str(out)], text=True).strip())
digest = hashlib.sha256(out.read_bytes()).hexdigest()

verification = {
    'record': '020',
    'status': 'published_unlistened',
    'routing_mode': 'exact_quote_locked',
    'uses_timestamps_for_speaker_assignment': False,
    'source_sha256': source_hash,
    'segment_count': 35,
    'ithar_segment_count': sum(1 for s in plan['segments'] if s['speaker'] == 'ithar'),
    'duration_seconds': round(duration, 3),
    'sha256': digest,
    'asset': asset,
    'note': 'Published by explicit user continuation request; deterministic route, speaker, and pause verification passed; auditory listen-back remains pending.'
}
(prod / 'verification-v2.json').write_text(json.dumps(verification, indent=2) + '\n', encoding='utf-8')

audio_path = root / 'audio/manifest.json'
audio = json.loads(audio_path.read_text(encoding='utf-8'))
audio['records']['r020'] = {
    'status': 'published',
    'src': asset,
    'source_sha256': source_hash,
    'audio_sha256': digest,
    'duration_seconds': round(duration, 3),
    'routing_mode': 'exact_quote_locked',
    'listened': False
}
audio_path.write_text(json.dumps(audio, indent=2) + '\n', encoding='utf-8')

manuscript_path = root / 'manuscript/manifest.json'
manuscript = json.loads(manuscript_path.read_text(encoding='utf-8'))
for rec in manuscript['records']:
    if rec['id'] == 'r020':
        rec['published'] = True
manuscript_path.write_text(json.dumps(manuscript, indent=2) + '\n', encoding='utf-8')

test_path = root / 'tests/test_repo_contract.py'
text = test_path.read_text(encoding='utf-8')
text = text.replace('self.assertTrue(all(r["published"] for r in records[:19]))', 'self.assertTrue(all(r["published"] for r in records[:20]))')
text = text.replace('self.assertTrue(all(not r["published"] for r in records[19:]))', 'self.assertTrue(all(not r["published"] for r in records[20:]))')
text = text.replace('self.assertTrue(all(audio["records"][f"r{i:03d}"]["status"] == "published" for i in range(1, 20)))', 'self.assertTrue(all(audio["records"][f"r{i:03d}"]["status"] == "published" for i in range(1, 21)))')
test_path.write_text(text, encoding='utf-8')
print(json.dumps(verification, indent=2))
