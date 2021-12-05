from gendiff.style_pack import plain_style, custom_style
import json
import yaml


def get_data(arg):
    if arg.endswith('.json'):
        return json.load(open(arg, 'r'))
    elif arg.endswith('.yaml') or arg.endswith('.yml'):
        return yaml.load(open(arg, 'r'), Loader=yaml.SafeLoader)


def generate_diff(first_arg, second_arg, format_style=None):

    data1 = get_data(first_arg)
    data2 = get_data(second_arg)

    result_diff = get_diff(data1, data2)

    if format_style == 'plain':
        output = plain_style.make_plain_stile(result_diff)
        return output

    elif format_style == 'json':
        return json.dumps(result_diff)

    elif format_style == 'yaml' or format_style == 'yml':
        result = yaml.dump(result_diff)
        return result

    else:
        output = custom_style.make_custom_style(result_diff)
        output = json.dumps(output, indent=4)
        output = output.replace('"', '').replace(',', '')
        output = output.replace('  +', '+').replace('  -', '-')
        return output


def get_diff(data1, data2):
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
                key1 = data1[key]
                key2 = data2[key]
                diff_result['nested'].update({key: get_diff(key1, key2)})

            elif data1[key] == data2[key]:
                diff_result['same'].update({key: data1.get(key)})

            else:
                diff_result['updated']['old_value'].update({key: data1[key]})
                diff_result['updated']['new_value'].update({key: data2[key]})

    return diff_result
