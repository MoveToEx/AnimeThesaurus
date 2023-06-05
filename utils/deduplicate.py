import sys
import json

with open(sys.argv[-1], 'r', encoding='utf8') as f:
    data = json.loads(f.read())

res = []

for i in data:
    kw = list(dict.fromkeys(sorted(i['keyword'])))
    content = list(dict.fromkeys(sorted(i['content'])))
    res.append({
        'keyword': kw,
        'content': content
    })


with open(sys.argv[-1], 'w', encoding='utf8') as f:
    f.write(json.dumps(res, ensure_ascii=False, indent=4))