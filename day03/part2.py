import argparse
import math
import sys
from typing import List

import pytest


def solve(input_string: str) -> int:
    lines = input_string.split()

    res = []

    for right, down in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
        count = 0
        i = 0

        for j in range(0, len(lines), down):
            if j == 0:
                continue

            line = lines[j]

            i += right
            if i >= len(line):
                i %= len(line)

            if line[i] == "#":
                count += 1

        res.append(count)

    return math.prod(res)


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
        (EXAMPLE_INPUT, 336),
    ),
)
def test(input_string: str, expected: int) -> None:
    assert solve(input_string) == expected


if __name__ == "__main__":
    main(sys.argv[1:])
