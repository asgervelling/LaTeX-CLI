from textwrap import dedent

import matrix


m_3x3 = [['a', 'b'],
         ['c', 'd']]


def create_matrix(m: list) -> str:
    '''
    \begin{bmatrix}
      a & b \\
      c & d
    \end{bmatrix}
    '''
    start_tag = '\\begin{bmatrix}'
    end_tag = '\end{bmatrix}'

    return dedent(
        f'{start_tag}\n' +
        f'{matrix.lines(m)}\n' +
        f'{end_tag}'
    )


print(create_matrix(m_3x3))


def encase_with_dollar_signs(text: str) -> str:
    return dedent(
        '$$\n' +
        f'{text}\n'
        '$$'
    )
