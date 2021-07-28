import argparse
import json


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', help='set format of output')

args = parser.parse_args()


def generate_diff(file1, file2):
    data1 = json.load(open(file1))
    data2 = json.load(open(file2))
    keys_data1 = set(data1.keys())
    keys_data2 = set(data2.keys())

    new_keys = keys_data2 - keys_data1
    removed_keys = keys_data1 - keys_data2
    common_keys = keys_data1 & keys_data2
    all_keys = sorted(new_keys | removed_keys | common_keys)
    diff_result = {}
    for key in all_keys:

        if key in new_keys:
            diff_result['+ ' + key] = data2.get(key)
        elif key in removed_keys:
            diff_result['- ' + key] = data1.get(key)
        else:
            if data1[key] == data2[key]:
                diff_result['  ' + key] = data1.get(key)
            else:
                diff_result['- ' + key] = data1.get(key)
                diff_result['+ ' + key] = data2.get(key)

    output = json.dumps(diff_result, indent=4).replace('"', '').replace(',', '')
    print(output)


generate_diff(args.first_file, args.second_file)
