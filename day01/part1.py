import argparse
import sys
from typing import List

import pytest


def solve(input_string: str) -> int:
    ints = [int(line) for line in input_string.split("\n")]

    hashtable = {}

    for x in ints:
        hashtable[2020 - x] = x

    for y in ints:
        if y in hashtable:
            return y * hashtable[y]

    return -1


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "infile", nargs="?", type=argparse.FileType("r"), default=sys.stdin
    )
    args = parser.parse_args(argv)
    print(solve(args.infile.read().strip()))
    return 0


@pytest.mark.parametrize(
    "input_string, expected",
    (
        # test cases
        ("1721\n979\n366\n299\n675\n1456", 514579),
    ),
)
def test(input_string: str, expected: int) -> None:
    assert solve(input_string) == expected


if __name__ == "__main__":
    main(sys.argv[1:])
