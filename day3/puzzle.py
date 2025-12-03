#!/usr/bin/env python3
"""
Advent of Code 2025 - Day Three
"""


def find_total_joltage(data: str, battery_count: int) -> int:
    return sum(find_joltage(bank, battery_count) for bank in data.split('\n'))


def find_joltage(bank: str, battery_count: int) -> int:
    previous_digit = None
    previous_bank = bank
    joltage = ''
    for i in range(battery_count, 0, -1):
        previous_pos = previous_bank.index(previous_digit) + 1 if previous_digit else 0
        if i > 1:
            new_bank = previous_bank[previous_pos:]
            next_digit = max(new_bank[:(-i)+1])
            previous_bank = new_bank
        else:
            new_bank = previous_bank[previous_pos:]
            next_digit = max(new_bank)
            previous_bank = new_bank
        joltage += f'{next_digit}'
        previous_digit = next_digit
    return int(joltage)


def main():

    with open('input.txt', 'r') as f:
        data = f.read()
        result = find_total_joltage(data.strip(), 12)
        print(f"Result: {result}")


if __name__ == "__main__":
    main()
