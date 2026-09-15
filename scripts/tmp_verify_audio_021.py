import hashlib, json, subprocess
from pathlib import Path
root=Path('.')
record='021'
source=root/f'manuscript/records/{record}/current.md'
routing=root/f'audio/routing/record-{record}.json'
plan_path=Path('/tmp/route-021.json')
subprocess.run(['python','scripts/audio_route.py',str(source),str(routing),str(plan_path)],check=True)
plan=json.loads(plan_path.read_text(encoding='utf-8'))
captures=json.loads((root/f'audio/production/record-{record}/captures.json').read_text(encoding='utf-8'))
source_hash=hashlib.sha256(source.read_bytes()).hexdigest()
assert source_hash=='95d98c85970eb0ec1d841d64bf8a84f96f1dece8354bfd020f9b6406f81edbc8'
assert plan['source_sha256']==captures['source_sha256']==source_hash
assert plan['routing_mode']==captures['routing_mode']=='exact_quote_locked'
assert captures['status']=='candidate_unlistened'
assert len(plan['segments'])==len(captures['segments'])==32
assert ''.join(s['transcript'] for s in plan['segments'])==plan['audio_body']
for i,(r,c) in enumerate(zip(plan['segments'],captures['segments']),1):
    assert r['index']==c['index']==i
    assert r['speaker']=='greg' and r['voice_id']=='deep'
    assert int(r['pause_after_ms'])==int(c['pause_after_ms'])
    assert c['preview_url'].startswith('https://')
print(json.dumps({'record':record,'source_sha256':source_hash,'segment_count':32,'status':'verified'}))
