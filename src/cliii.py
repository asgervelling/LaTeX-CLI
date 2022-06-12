import sys


def read_input():
    if sys.stdin.isatty():
        # _input = prepare_args()
        _input = sys.argv[1:]
    else:
        _input = sys.stdin.readlines()

    args = as_arg_list(_input)
    print(args)


def as_arg_list(_input):
    """ Turn the entire _input list into a string, 
        insert a pipe character in all the places where 
        the arguments should be split up.
        Return the list of arguments. """
    input_str = ''.join(_input).strip()
    delimited_str = _delimit_input_str(input_str)
    return delimited_str.split('|')


def _delimit_input_str(_input: str) -> str:
    return _input \
        .replace('\n', '|') \
        .replace('{', '|{|') \
        .replace('}', '|}|') \
        .replace('||', '|')


def prepare_stdin():
    pass


def prepare_args():
    _input = sys.argv[1:]
    print(as_arg_list(_input))
    return _input


def read_stdin():
    print('read_stdin()')

    print('|'.join(sys.stdin))

    """ for line in sys.stdin:
        sys.stdout.write('\t' + line) """


def read_args():
    print('read_args()')

    print('|'.join(sys.argv[1:]))

    """ for arg in sys.argv:
        sys.stdout.write('\t' + arg + '\n') """


if __name__ == '__main__':
    read_input()
