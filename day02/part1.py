import argparse
import sys
from typing import List

import pytest


def solve(input_string: str) -> int:
    res = 0
    for line in input_string.split("\n"):
        interval, letter, password = line.split(" ")
        letter = letter[:-1]
        left, right = [int(i) for i in interval.split("-")]
        letter_count = password.count(letter)
        if left <= letter_count <= right:
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


@pytest.mark.parametrize(
    "input_string, expected",
    (
        # test cases
        ("1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc", 2),
    ),
)
def test(input_string: str, expected: int) -> None:
    assert solve(input_string) == expected


if __name__ == "__main__":
    main(sys.argv[1:])
