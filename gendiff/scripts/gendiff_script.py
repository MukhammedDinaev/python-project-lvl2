from gendiff import engine
from gendiff import gendiff_args


def main():
    first_arg = gendiff_args.args.first_file
    second_arg = gendiff_args.args.second_file
    return engine.run_diff(first_arg, second_arg)


if __name__ == '__main__':
    main()
