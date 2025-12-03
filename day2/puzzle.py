#!/usr/bin/env python3
"""
Advent of Code 2025 - Day Two
"""

import re


def find_invalid_id_sum(data: str) -> int:
    id_ranges = data.split(',')
    sum = 0
    for id_range in id_ranges:
        if '-' in id_range:
            start, end = id_range.split('-')
            sum += find_repeating_id_sum(int(start), int(end))
    return sum


def find_repeating_id_sum(start: int, end: int) -> int:
    sum = 0
    for i in range(start, end):
        id_str = str(i)
        for j in range(len(id_str)//2):
            id_str_left = id_str[:j+1]
            pattern = re.compile(f"^({id_str_left})+$")
            if pattern.match(id_str):
                sum += i
                break
    return sum


def main():

    with open('input.txt', 'r') as f:
        data = f.read()
        result = find_invalid_id_sum(data)
        print(f"Result: {result}")


if __name__ == "__main__":
    main()
