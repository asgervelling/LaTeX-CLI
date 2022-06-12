from typing import List
import sys


def get_symbols() -> List[List[str]]:
    clean_symbols = read_input_symbols()
    valid = validate(clean_symbols)


def validate(symbols: List[List[str]]) -> bool:
    """ 
            Valid input:    ['matrix ', '{', 'a b', 'c d', 'e f', '}'] 
            Invalid:        ['matrix ', '{', 'a b c', 'c d', 'e f', '}'] 
            Invalid:        ['matrix ', 'a b', 'c d', 'e f', '}']

    'matrix':   Next symbol must be '{'.
    '{':        There must be a '}' later.
    'a b'       Symbols before '}' must have the same number of strings when split on ' ', e.g.:

                    'a b' -> ['a', 'b'] (length: 2)
                    'c d' is valid, because len(['c', 'd']) == 2
                    'c d e' is not valid, because len(['c', 'd', 'e']) != 2

    Different kinds of rules:
    The '{'-rule is persistent. While iterating through the symbols, after reading '{',
    the function is looking for a '}'. If at the end of the symbols list, the character '}' is
    still not found, then the list of symbols is invalid.

    The 'a b' rule is not persistent. If a symbol is 'a b c' (length: 3), then the next symbol
    must also be of length 3.

    """

    if symbols[0] == 'matrix':
        return validate_matrix(symbols)


def validate_matrix(symbols: List[List[str]]) -> bool:
    if validate_open_close_symbols(symbols) == False: 
        return False
    
    inner = inner_symbols(symbols, s0='{', s1='}')
    space_delimited = [s.split(sep=' ')
                       for s
                       in inner]

    # All rows in the matrix must have the same length
    return all(len(space_delimited[0]) == len(row) for row in space_delimited[1:])
    


def validate_open_close_symbols(symbols: List[List[str]]) -> bool:
    """ There should be the same number of '{' as '}'.
        The same goes for '[' and ']' and '(' and ')', if the need arises. """
    closing_symbols = {
        '}': 0
    }
    for symbol in symbols:
        if symbol == '{':
            closing_symbols['}'] -= 1
        if symbol == '}':
            closing_symbols['}'] += 1

    return all([val == 0 for val in closing_symbols.values()])


def inner_symbols(symbols: List[List[str]], s0: str, s1: str) -> List[List[str]]:
    """ Get the symbols between s0 and s1. Ex.:
            symbols:    ['matrix ', '{', 'a b', 'c d', 'e f', '}'] 
            s0:         '{' 
            s1:         '}'

            -> ['a b', 'c d', 'e f']    
    """
    i0 = symbols.index(s0) + 1
    i1 = symbols.index(s1)
    return symbols[i0:i1]


def get_input_symbols() -> List[List[str]]:
    if sys.stdin.isatty():
        raw_input = sys.argv[1:]
    else:
        raw_input = sys.stdin.readlines()

    args = clean(raw_input)
    return args


def _remove_empty(_input: List[List[str]]) -> List[List[str]]:
    """ Remove empty strings """
    return list(filter(None, _input))


def read_input_symbols(_input: List[List[str]]) -> List[List[str]]:
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


def clean(_input: List[List[str]]) -> List[List[str]]:
    input_symbols = read_input_symbols(_input)
    stripped = list(map(str.strip, input_symbols))
    empties_removed = _remove_empty(stripped)
    lowered = list(map(str.lower, empties_removed))
    return lowered
