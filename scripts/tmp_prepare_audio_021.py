import json, subprocess
from pathlib import Path

root=Path('.')
record='021'
source=root/f'manuscript/records/{record}/current.md'
routing=root/f'audio/routing/record-{record}.json'
prod=root/f'audio/production/record-{record}'
prod.mkdir(parents=True, exist_ok=True)
route=prod/'route-plan.json'
subprocess.run(['python','scripts/audio_route.py',str(source),str(routing),str(route)],check=True)
plan=json.loads(route.read_text(encoding='utf-8'))
assert plan['record']==record
assert plan['routing_mode']=='exact_quote_locked'
assert ''.join(s['transcript'] for s in plan['segments'])==plan['audio_body']
for s in plan['segments']:
    assert s['speaker']=='greg' and s['voice_id']=='deep'
segments=plan['segments']
for start in range(0,len(segments),10):
    chunk=segments[start:start+10]
    out=prod/'work-orders'/f"segments-{chunk[0]['index']:03d}-{chunk[-1]['index']:03d}.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps({'record':record,'source_sha256':plan['source_sha256'],'routing_mode':plan['routing_mode'],'segments':chunk},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'record':record,'source_sha256':plan['source_sha256'],'segment_count':len(segments)}))
