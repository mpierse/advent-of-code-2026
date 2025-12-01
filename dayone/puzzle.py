#!/usr/bin/env python3
"""
Advent of Code 2025 - Day One
"""


def turn_dial(directions: str) -> int:
    # Starting at a very high number to avoid negative numbers
    current_position = 100000000050
    zero_count = 0
    for direction in directions.split('\n'):
        if not direction:  # Skip empty lines
            continue
            
        turn_start = current_position
        count = int(direction[1:])
        if 'L' in direction:
            current_position -= count
        elif 'R' in direction:
            current_position += count
        turn_end = current_position

        # Count all multiples of 100 crossed during this turn
        # We need different formulas for left vs right:
        # - Right (end > start): multiples in (start, end] = floor(end/100) - floor(start/100)
        # - Left (end < start): multiples in [end, start) = floor((start-1)/100) - floor((end-1)/100)
        if turn_end > turn_start:
            # Moving right: count multiples in (start, end]
            zero_count += turn_end // 100 - turn_start // 100
        else:
            # Moving left: count multiples in [end, start)
            # Need to subtract 1 from start and end catch ending on a multiple of 100
            zero_count += (turn_start - 1) // 100 - (turn_end - 1) // 100

    return zero_count


def main():

    with open('input.txt', 'r') as f:
        data = f.read()
        result = turn_dial(data)
        print(f"Result: {result}")


if __name__ == "__main__":
    main()
