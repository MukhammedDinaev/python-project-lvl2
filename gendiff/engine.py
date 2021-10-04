from gendiff import generate_diff
from gendiff.style_pack import plain_style, custom_style
import json
import yaml


def get_data(arg):
    if arg.endswith('.json'):
        return json.load(open(arg, 'r'))
    elif arg.endswith('.yaml') or arg.endswith('.yml'):
        return yaml.load(open(arg, 'r'), Loader=yaml.SafeLoader)


def run_diff(first_arg, second_arg, format_style=None):

    data1 = get_data(first_arg)
    data2 = get_data(second_arg)

    result_diff = generate_diff.generate_diff(data1, data2)

    if format_style == 'plain':
        output = plain_style.make_plain_stile(result_diff)
        print(output)
        return output

    else:
        output = custom_style.make_custom_style(result_diff)
        output = json.dumps(output, indent=4).replace('"', '').replace(',', '')
        output = output.replace('  +', '+').replace('  -', '-')
        print(output)
        return output
