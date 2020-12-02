import argparse
import sys
from typing import List

import pytest


def solve(input_string: str) -> int:
    res = 0
    for line in input_string.split("\n"):
        positions, letter, password = line.split(" ")
        letter = letter[:-1]
        i, j = [int(i) - 1 for i in positions.split("-")]
        if password[i] == password[j]:
            continue
        if password[i] == letter or password[j] == letter:
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
        ("1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc", 1),
    ),
)
def test(input_string: str, expected: int) -> None:
    assert solve(input_string) == expected


if __name__ == "__main__":
    main(sys.argv[1:])
