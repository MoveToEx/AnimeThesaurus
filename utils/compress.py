
import sys
import json

if not sys.argv[-1].endswith('.json'):
    print("Invalid input file")
    exit(1)

with open(sys.argv[-1], 'r', encoding='utf8') as f:
    data = json.loads(f.read())

with open(sys.argv[-1].removesuffix('.json') + '.min.json', 'w', encoding='utf8') as f:
    f.write(json.dumps(data, ensure_ascii=False))