from gendiff import generate_diff
from gendiff import gendiff_args


def main():
    first_arg = gendiff_args.args.first_file
    second_arg = gendiff_args.args.second_file
    format_style = gendiff_args.args.format
    return generate_diff.generate_diff(first_arg, second_arg, format_style)


if __name__ == '__main__':
    main()
