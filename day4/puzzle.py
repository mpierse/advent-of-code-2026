#!/usr/bin/env python3
"""
Advent of Code 2025 - Day Four
"""

DIRECTIONS_8 = [
    (-1, 0),   # up
    (1, 0),    # down
    (0, -1),   # left
    (0, 1),    # right
    (-1, -1),  # up-left
    (-1, 1),   # up-right
    (1, -1),   # down-left
    (1, 1),    # down-right
]


def total_accessible_rolls(data: str) -> int:
    grid = data.split('\n')
    roll_count = 0
    last_roll_count = -1
    updated_grid = grid
    while last_roll_count != 0:
        last_roll_count, updated_grid = accessible_roll_count(updated_grid)
        roll_count += last_roll_count
    return roll_count


def accessible_roll_count(grid: list[str]) -> tuple[int, list[str]]:
    accessible_rolls = 0
    new_grid = []
    for y in range(len(grid)):
        new_row = []
        for x in range(len(grid[y])):
            if is_accessible(grid, x, y):
                accessible_rolls += 1
                new_row.append('.')
            else:
                new_row.append(grid[y][x])
        new_grid.append(''.join(new_row))
    return accessible_rolls, new_grid


def is_accessible(grid: list[str], x: int, y: int) -> bool:
    if grid[y][x] == '@':
        neighboring_rolls = 0
        for direction in DIRECTIONS_8:
            new_x = x + direction[0]
            new_y = y + direction[1]
            if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
                if grid[new_y][new_x] == '@':
                    neighboring_rolls += 1
        return neighboring_rolls < 4
    return False


def main():
    with open('input.txt', 'r') as f:
        data = f.read()
        result = total_accessible_rolls(data)
        print(f"Result: {result}")


if __name__ == "__main__":
    main()
