import yaml

data = yaml.load(open('filepath2.yaml', 'r'), Loader=yaml.BaseLoader)


print(data)
print(set(data.keys()))
