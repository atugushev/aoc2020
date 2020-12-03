import argparse
import sys
from typing import List

import pytest


def solve(input_string: str) -> int:
    lines = input_string.split()

    i = 0
    res = 0

    for j, line in enumerate(lines):
        if j == 0:
            continue

        i += 3
        if i >= len(line):
            i %= len(line)

        if line[i] == "#":
            res += 1

    return res


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "infile", nargs="?", type=argparse.FileType("r"), default=sys.stdin
    )
    args = parser.parse_args(argv)
    print(solve(args.infile.read().strip()))
    return 0


EXAMPLE_INPUT = """\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#\
"""


@pytest.mark.parametrize(
    "input_string, expected",
    (
        # test cases
        (EXAMPLE_INPUT, 7),
    ),
)
def test(input_string: str, expected: int) -> None:
    assert solve(input_string) == expected


if __name__ == "__main__":
    main(sys.argv[1:])
