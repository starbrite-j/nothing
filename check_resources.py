"""Guards against compiler symbol aliasing and broken native references."""
from pathlib import Path
from collections import defaultdict
import json
ROOT=Path(__file__).resolve().parent
symbols=defaultdict(list);ids=defaultdict(list);resources=[]
for p in (ROOT/'project').rglob('*.gbsres'):
    r=json.loads(p.read_text());resources.append((p,r))
    if r.get('symbol'):symbols[r['symbol']].append(str(p.relative_to(ROOT)))
    if r.get('id'):ids[r['id']].append(str(p.relative_to(ROOT)))
assert not {s:p for s,p in symbols.items() if len(p)>1}, 'Duplicate compiler symbol'
assert not {s:p for s,p in ids.items() if len(p)>1}, 'Duplicate resource ID'
sceneids={r['id'] for _,r in resources if r.get('_resourceType')=='scene'}
def walk(value):
    if isinstance(value,dict):
        if value.get('command')=='EVENT_SWITCH_SCENE':
            assert value['args']['sceneId'] in sceneids,value
        for v in value.values():walk(v)
    elif isinstance(value,list):
        for v in value:walk(v)
for _,r in resources:walk(r)
print(f'PASS: {len(resources)} resource files; unique symbols and IDs; all scene transitions resolve.')
