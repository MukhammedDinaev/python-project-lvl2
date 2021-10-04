import json
import yaml

f1 = json.load(open('filetree1.json'))
f2 = json.load(open('filetree2.json'))

f4 = open('filetree1.yaml', 'w')
f4.write(yaml.dump(f1))

f5 = open('filetree2.yaml', 'w')
f5.write(yaml.dump(f2))
