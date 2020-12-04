import argparse
import re
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
    for i in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"):
        if i not in data:
            return False

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if not (1920 <= int(data["byr"]) <= 2002):
        return False

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if not (2010 <= int(data["iyr"]) <= 2020):
        return False

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if not (2020 <= int(data["eyr"]) <= 2030):
        return False

    # hgt (Height) - a number followed by either cm or in:
    m = re.match(r"(\d+)(cm|in)$", data["hgt"])
    if not m:
        return False

    # If cm, the number must be at least 150 and at most 193.
    if m[2] == "cm" and not (150 <= int(m[1]) <= 193):
        return False

    # If in, the number must be at least 59 and at most 76.
    if m[2] == "in" and not (59 <= int(m[1]) <= 76):
        return False

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if not (re.match("^#[a-f0-9]{6}$", data["hcl"])):
        return False

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if data["ecl"] not in set("amb blu brn gry grn hzl oth".split(" ")):
        return False

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if not (re.match("^[0-9]{9}$", data["pid"])):
        return False

    # cid (Country ID) - ignored, missing or not.

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
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719\
"""


@pytest.mark.parametrize(
    "input_string, expected",
    (
        # test cases
        (EXAMPLE_INPUT, 4),
    ),
)
def test(input_string: str, expected: int) -> None:
    assert solve(input_string) == expected


if __name__ == "__main__":
    main(sys.argv[1:])
