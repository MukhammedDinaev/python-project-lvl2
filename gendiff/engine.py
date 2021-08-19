from gendiff import generate_diff
import json
import yaml


def get_data(arg):
    if arg.endswith('.json'):
        return json.load(open(arg, 'r'))
    elif arg.endswith('.yaml') or arg.endswith('.yml'):
        return yaml.load(open(arg, 'r'), Loader=yaml.BaseLoader)


def run_diff(first_arg, second_arg):

    data1 = get_data(first_arg)
    data2 = get_data(second_arg)

    result_diff = generate_diff.generate_diff(data1, data2)
    output = json.dumps(result_diff, indent=4).replace('"', '').replace(',', '')
    output = output.replace('  +', '+').replace('  -', '-')
    print(output)
    return output
