import argparse
import sys
from typing import Dict, List

import pytest


def solve(input_string: str) -> int:
    res = 0
    for line in input_string.split("\n\n"):
        line = line.replace("\n", " ")
        if not line:
            continue

        data: Dict[str, str] = dict(x.partition(":")[::2] for x in line.split(" "))
        if validate(data):
            res += 1

    return res


def validate(data: Dict[str, str]) -> bool:
    print(data)
    for i in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"):
        if i not in data:
            return False
    return True


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "infile", nargs="?", type=argparse.FileType("r"), default=sys.stdin
    )
    args = parser.parse_args(argv)
    print(solve(args.infile.read().strip()))
    return 0


EXAMPLE_INPUT = """\
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in\
"""


@pytest.mark.parametrize(
    "input_string, expected",
    (
        # test cases
        (EXAMPLE_INPUT, 2),
    ),
)
def test(input_string: str, expected: int) -> None:
    assert solve(input_string) == expected


if __name__ == "__main__":
    main(sys.argv[1:])
