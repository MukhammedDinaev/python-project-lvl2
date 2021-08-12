import argparse
from gendiff import generate_diff as gd


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', help='set format of output')

args = parser.parse_args()

generate_diff = gd.generate_diff(args.first_file, args.second_file)
print(generate_diff)
