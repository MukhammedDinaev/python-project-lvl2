import json
import yaml

def generate_diff(data1, data2):
    keys_data1 = set(data1.keys())
    keys_data2 = set(data2.keys())

    new_keys = keys_data2 - keys_data1
    removed_keys = keys_data1 - keys_data2
    common_keys = keys_data1 & keys_data2
    all_keys = sorted(new_keys | removed_keys | common_keys)

    diff_result = {}
    diff_result['added'] = {}
    diff_result['removed'] = {}
    diff_result['updated'] = {'old_value': {}, 'new_value': {}}
    diff_result['nested'] = {}
    diff_result['same'] = {}
    diff_result['all_keys'] = all_keys

    for key in all_keys:
        if key in new_keys:
            diff_result['added'].update({key: data2.get(key)})

        elif key in removed_keys:
            diff_result['removed'].update({key: data1.get(key)})

        elif key in common_keys:
            if type(data1[key]) == dict and type(data2[key]) == dict:
                diff_result['nested'].update({key: generate_diff(data1[key], data2[key])})

            elif data1[key] == data2[key]:
                diff_result['same'].update({key: data1.get(key)})

            else:
                diff_result['updated']['old_value'].update({key: data1.get(key)})
                diff_result['updated']['new_value'].update({key: data2.get(key)})

    return diff_result


#file1 = json.load((open('../tests/fixtures/filetree1.json', 'r')))
#file2 = json.load((open('../tests/fixtures/filetree2.json', 'r')))
file1 = yaml.load(open('../tests/fixtures/filetree1.yaml', 'r'), Loader=yaml.BaseLoader)
file2 = yaml.load(open('../tests/fixtures/filetree2.yaml', 'r'), Loader=yaml.BaseLoader)

res1 = generate_diff(file1, file2)

#res1 = json.dumps(res1, indent=4).replace('"', '').replace(',', '').replace('  +', '+').replace('  -', '-')
#print(res1)


def stilysh(diff):
    all_keys = diff['all_keys']
    output = {}
    if len(all_keys) > 0:
        for key in all_keys:
            if key in diff['added']:
                output['+ ' + key] = diff['added'].get(key)
            elif key in diff['removed']:
                output['- ' + key] = diff['removed'].get(key)
            elif key in diff['updated']['old_value']:
                output['- ' + key] = diff['updated']['old_value'].get(key)
                output['+ ' + key] = diff['updated']['new_value'].get(key)
            elif key in diff['updated']['new_value']:
                output['- ' + key] = diff['updated']['old_value'].get(key)
                output['+ ' + key] = diff['updated']['new_value'].get(key)
            elif key in diff['nested']:
                output[key] = stilysh(diff['nested'].get(key))
            elif key in diff['same']:
                output[key] = diff['same'][key]
    return output


def is_in_group(group, value):
    return value in group


def get_value(value):
    if type(value) == str:
        return '\'{}\''.format(value)
    elif value is None:
        return 'null'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif not type(value) == dict:
        return value
    return '[complex value]'


def make_plain_stile(diff_data, path='', result=None):
    if result is None:
        result = []
    all_keys = diff_data['all_keys']
    if all_keys:
        for key in all_keys:
            if is_in_group(diff_data['added'], key):
                path1 = path + key
                value = get_value(diff_data['added'][key])
                result.append('Property \'{}\' was added with value: {}'.format(path1, value))
            elif is_in_group(diff_data['removed'], key):
                path1 = path + key
                result.append('Property \'{}\' was removed'.format(path1))
            elif is_in_group(diff_data['updated']['old_value'], key):
                path1 = path + key
                old_value = get_value(diff_data['updated']['old_value'][key])
                new_value = get_value(diff_data['updated']['new_value'][key])
                result.append('Property \'{}\' was updated. From {} to {}'.format(path1, old_value, new_value))
            elif is_in_group(diff_data['nested'], key):
                make_plain_stile(diff_data['nested'][key], path + key + '.', result)
    return '\n'.join(result)


print(make_plain_stile(res1))


res2 = stilysh(res1)
res2 = json.dumps(res2, indent=4).replace('"', '').replace(',', '').replace('  +', '+').replace('  -', '-')
#res2 = json.dumps(res1, indent=4).replace('"', '').replace(',', '').replace('  +', '+').replace('  -', '-')
print(res2)

print(res2)