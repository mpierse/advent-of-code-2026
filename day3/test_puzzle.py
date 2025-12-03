#!/usr/bin/env python3
"""
Tests for Advent of Code 2025 - Day Three
"""

import unittest
from puzzle import find_total_joltage, find_joltage


# class TestFindJoltage(unittest.TestCase):
#     """Test the find_joltage function"""

#     def test_single_max_digit_at_end(self):
#         """Test when max digit appears once at the end"""
#         result = find_joltage('12349', 2)
#         self.assertEqual(result, 49)

#     def test_single_max_digit_in_middle(self):
#         """Test when max digit appears once in the middle"""
#         # Max is 9, split gives ['123', '456'], second digit is max of '456' = '6'
#         result = find_joltage('1239456', 2)
#         self.assertEqual(result, 96)

#     def test_two_max_digits(self):
#         """Test when max digit appears twice"""
#         # Max is 9, split gives ['12', '34', ''], there are 2 max digets so '99
#         result = find_joltage('129349', 2)
#         self.assertEqual(result, 99)

#     def test_three_max_digits(self):
#         """Test when max digit appears three or more times"""
#         # Max is 9, split gives multiple segments, second digit equals first digit
#         result = find_joltage('192939', 2)
#         self.assertEqual(result, 99)

#     def test_all_same_digit(self):
#         """Test when all digits are the same"""
#         # Max is 7, split gives ['', '', '', ''], after removing '' we get []
#         result = find_joltage('77779', 2)
#         self.assertEqual(result, 79)

#     def test_max_digit_at_start(self):
#         """Test when max digit is at the start"""
#         # Max is 9, split gives ['', '12345'], second digit is max of '12345' = '5'
#         result = find_joltage('912354', 2)
#         self.assertEqual(result, 95)

#     def test_two_digits(self):
#         """Test two digit bank with max at end"""
#         # Max is 8, split gives ['1'], second digit is max of '1' = '1'
#         result = find_joltage('18', 2)
#         self.assertEqual(result, 18)

#     def test_all_max_at_end(self):
#         """Test alternating max digits"""
#         # Max is 9, appears 4 times, should return 99
#         result = find_joltage('435245399', 2)
#         self.assertEqual(result, 99)


class TestFindTotalJoltage(unittest.TestCase):
    """Test the find_total_joltage function"""

#     def test_single_battery_bank(self):
#         """Test with a single battery bank"""
#         data = "12349"
#         result = find_total_joltage(data, 2)
#         self.assertEqual(result, 49)

#     def test_multiple_battery_banks(self):
#         """Test with multiple battery banks separated by newlines"""
#         data = "12349\n1239456\n129349"
#         result = find_total_joltage(data, 2)
#         expected = 49 + 96 + 99
#         self.assertEqual(result, expected)

#     def test_many_large_battery_banks(self):
#         """Test with many battery banks"""
#         data = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111
# 453467254763498
# 111111111111111"""
#         result = find_total_joltage(data, 2)
#         expected = 98 + 89 + 78 + 92 + 98 + 11
#         self.assertEqual(result, expected)

#     def test_banks_with_many_max_occurrences(self):
#         """Test banks where max digit appears many times"""
#         data = "91929394\n81828384"
#         result = find_total_joltage(data, 2)
#         expected = 99 + 88
#         self.assertEqual(result, expected)

    def test_many_large_battery_banks_with_11_batteries(self):
        """Test with many battery banks"""
        data = """987654321111111
811111111111119
234234234234278
818181911112111"""
        result = find_total_joltage(data, 12)
        expected = 987654321111 + 811111111119 + 434234234278 + 888911112111
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

