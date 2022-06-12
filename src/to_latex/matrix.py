from typing import List


def and_symbols(matrix: List[List[str]]) -> List[List[str]]:
    return [' & '.join(line) for line in matrix]


def right_spacing(matrix: List[List[str]]) -> List[List[str]]:
    return [f'  {line}' for line in matrix]


def line_separators(matrix: List[List[str]]) -> str:
    return ' \\\\\n'.join(matrix)


def lines(matrix: List[List[str]]) -> str:
    return line_separators(
        right_spacing(
            and_symbols(matrix)
        )
    )
