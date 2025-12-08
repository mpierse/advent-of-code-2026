#!/usr/bin/env python3
"""
Advent of Code 2025 - Day Five
"""
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def total_fresh_ingredients(data: str) -> int:
    ingredients = data.split('\n\n')
    fresh_ingredient_ranges = ingredients[0].split('\n')
    available_ingredient_ids = ingredients[1].split('\n')

    total_fresh_ingredients = 0

    for id in available_ingredient_ids:
        for fresh_ingredient_range in fresh_ingredient_ranges:
            start, end = fresh_ingredient_range.split('-')
            if int(id) >= int(start) and int(id) <= int(end):
                total_fresh_ingredients += 1
                break
    return total_fresh_ingredients


def possible_fresh_ingredients(data: str) -> int:
    logger.debug("Starting possible_fresh_ingredients calculation")
    ingredients = data.split('\n\n')
    fresh_ingredient_ranges = ingredients[0].split('\n')

    ranges = []
    for range_str in fresh_ingredient_ranges:
        start, end = range_str.split('-')
        ranges.append((int(start), int(end)))

    # Sort ranges by start value
    ranges.sort(key=lambda x: x[0])

    # Merge overlapping ranges
    merged_ranges = []
    for start, end in ranges:
        if len(merged_ranges) == 0:
            merged_ranges.append((start, end))
        else:
            last_start, last_end = merged_ranges[-1]
            if start <= last_end or start == last_start:
                merged_ranges[-1] = (last_start, max(last_end, end))
            else:
                merged_ranges.append((start, end))

    total_possible_fresh_ingredients = 0
    for s, e in merged_ranges:
        count = e - s + 1 # +1 because both endpoints are inclusive
        logger.debug(f"Range ({s}, {e}) contributes {count} ingredients")
        total_possible_fresh_ingredients += count

    logger.info(f"Total possible fresh ingredients: {total_possible_fresh_ingredients}")
    return total_possible_fresh_ingredients


def main():
    with open('input.txt', 'r') as f:
        data = f.read()
        result = possible_fresh_ingredients(data)
        print(f"Result: {result}")


if __name__ == "__main__":
    main()
