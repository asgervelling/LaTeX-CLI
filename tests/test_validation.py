import pytest

from src.cli.validation import clean, inner_symbols, read_input_symbols, validate_matrix, validate_open_close_symbols


def test_validate_open_close_symbols():
    assert validate_open_close_symbols(['matrix ', 'a b', 'c d', 'e f', '}']) == False
    assert validate_open_close_symbols(['matrix ', '{', 'a b', 'c d', 'e f', '}']) == True
    assert validate_open_close_symbols(['{', '{', '}']) == False
    assert validate_open_close_symbols(['{', '}', '{', '}']) == True


def test_inner_symbols():
    assert inner_symbols(['matrix ', '{', 'a b', 'c d', 'e f', '}'], s0='{', s1='}') \
        == ['a b', 'c d', 'e f']
    with pytest.raises(ValueError):
        inner_symbols(['matrix ', '{', 'a b', 'c d', 'e f'], s0='{', s1='}')


def test_clean():
    raw_input_0 = '''maTRix {
        a b
        c d
        }
    '''
    assert clean(raw_input_0) == ['matrix', '{', 'a b', 'c d', '}']


def test_validate_matrix():
    raw_input_0 = '''maTRix {
        a b
        c d
        }
    '''
    raw_input_1 = '''maTRix {
        a b c
        c d
        }
    '''
    raw_input_2 = '''maTRix {
        a b
        c d
    '''
    cleaned_0 = clean(raw_input_0)
    cleaned_1 = clean(raw_input_1)
    cleaned_2 = clean(raw_input_1)
    assert validate_matrix(cleaned_0) == True
    assert validate_matrix(cleaned_1) == False
    assert validate_matrix(cleaned_2) == False