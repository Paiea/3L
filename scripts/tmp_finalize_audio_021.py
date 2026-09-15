import hashlib, json
from pathlib import Path

root=Path('.')
record='021'
source=root/f'manuscript/records/{record}/current.md'
prod=root/f'audio/production/record-{record}'
verification=json.loads((prod/'verification-v2.json').read_text(encoding='utf-8'))
asset=root/verification['asset']
source_hash=hashlib.sha256(source.read_bytes()).hexdigest()
assert source_hash==verification['source_sha256']=='95d98c85970eb0ec1d841d64bf8a84f96f1dece8354bfd020f9b6406f81edbc8'
assert verification['segment_count']==32
assert verification['status']=='published_unlistened'
assert hashlib.sha256(asset.read_bytes()).hexdigest()==verification['sha256']=='d2d9282d2b733c8f3e444e97857e364a1a57f9f7daca0f3d37c9def83e8dc502'

audio_path=root/'audio/manifest.json'
audio=json.loads(audio_path.read_text(encoding='utf-8'))
audio['records']['r021']={
  'status':'published',
  'src':verification['asset'],
  'source_sha256':source_hash,
  'audio_sha256':verification['sha256'],
  'duration_seconds':verification['duration_seconds'],
  'routing_mode':'exact_quote_locked',
  'listened':False
}
audio_path.write_text(json.dumps(audio,indent=2)+'\n',encoding='utf-8')

manifest_path=root/'manuscript/manifest.json'
manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
def wc(path):
    return sum(1 for token in path.read_text(encoding='utf-8').split() if token!='##')
reconciled=[]
for rec in manifest['records'][10:]:
    current=root/rec['path']
    original=root/'manuscript'/'records'/rec['slot']/'versions'/'original-run.md'
    if current.read_bytes()!=original.read_bytes() and rec['prose_status']=='needs_rehearsal':
        rec['prose_status']='restored'
        rec['word_count']=wc(current)
        reconciled.append(rec['id'])
    if rec['id']=='r021':
        rec['published']=True
manifest_path.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')

test_path=root/'tests/test_repo_contract.py'
text=test_path.read_text(encoding='utf-8')
text=text.replace('self.assertTrue(all(r["published"] for r in records[:20]))','self.assertTrue(all(r["published"] for r in records[:21]))')
text=text.replace('self.assertTrue(all(not r["published"] for r in records[20:]))','self.assertTrue(all(not r["published"] for r in records[21:]))')
text=text.replace('self.assertTrue(all(audio["records"][f"r{i:03d}"]["status"] == "published" for i in range(1, 21)))','self.assertTrue(all(audio["records"][f"r{i:03d}"]["status"] == "published" for i in range(1, 22)))')
test_path.write_text(text,encoding='utf-8')
print(json.dumps({'record':'021','reconciled':reconciled,'duration_seconds':verification['duration_seconds']},indent=2))
