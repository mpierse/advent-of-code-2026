#!/usr/bin/env python3
"""
Tests for Advent of Code 2025 - Day Two
"""

import unittest
from puzzle import find_invalid_id_sum, find_repeating_id_sum


class TestFindRepeatingIdSum(unittest.TestCase):
    """Test the find_repeating_id_sum function"""

    def test_simple_range_with_repeating_ids(self):
        """Test a range that contains repeating IDs"""
        # Range 1000-1500 should include even repeating IDs like 1212, 1414
        result = find_repeating_id_sum(1000, 1500)
        # 1212, 1414 are the repeating even numbers in this range
        expected = 1010 + 1111 + 1212 + 1313 + 1414
        self.assertEqual(result, expected)

    def test_range_with_single_repeating_id(self):
        """Test a range with just one repeating ID"""
        # Range 1200-1220 should include 1212
        result = find_repeating_id_sum(1200, 1220)
        self.assertEqual(result, 1212)

    def test_range_with_no_repeating_ids(self):
        """Test a range with no repeating IDs"""
        # Range 100-200 has no 4-digit repeating numbers
        result = find_repeating_id_sum(123, 126)
        self.assertEqual(result, 0)

    def test_small_range(self):
        """Test a very small range"""
        result = find_repeating_id_sum(1, 10)
        self.assertEqual(result, 0)

    def test_six_digit_repeating_ids(self):
        """Test with 6-digit repeating IDs"""
        # Range 123000-124000 should include 123123
        result = find_repeating_id_sum(123000, 124000)
        self.assertEqual(result, 123123)


class TestFindInvalidIdSum(unittest.TestCase):
    """Test the find_invalid_id_sum function"""

    def test_single_range(self):
        """Test with a single range"""
        data = "1200-1220"
        result = find_invalid_id_sum(data)
        # Should find 1212
        self.assertEqual(result, 1212)

    def test_multiple_ranges(self):
        """Test with multiple comma-separated ranges"""
        data = "95-115,1200-1220,1400-1420"
        result = find_invalid_id_sum(data)

        expected = 99 + 111 + 1212 + 1414
        self.assertEqual(result, expected)

    def test_three_ranges(self):
        """Test with three ranges"""
        data = "1200-1220,1400-1420,1600-1620"
        result = find_invalid_id_sum(data)
        # Should find 1212, 1414, and 1616
        expected = 1212 + 1414 + 1616
        self.assertEqual(result, expected)

    def test_range_with_no_repeating_ids(self):
        """Test with a range that has no repeating IDs"""
        data = "1698522-1698528"
        result = find_invalid_id_sum(data)
        self.assertEqual(result, 0)

    def test_non_range_values_ignored(self):
        """Test that values without hyphens are ignored"""
        data = "1000,1200-1220,2000"
        result = find_invalid_id_sum(data)
        # Only 1200-1220 range is processed
        self.assertEqual(result, 1212)

    def test_empty_string(self):
        """Test with empty string"""
        data = ""
        result = find_invalid_id_sum(data)
        self.assertEqual(result, 0)

    def test_large_range(self):
        """Test with a large range"""
        data = "1000-2000"
        result = find_invalid_id_sum(data)
        expected = (1010 + 1111 + 1212 + 1313 + 1414 + 1515 + 1616 + 1717
                    + 1818 + 1919)
        self.assertEqual(result, expected)

    def test_multiple_ranges_some_empty(self):
        """Test multiple ranges where some yield no results"""
        data = "100-200,1200-1220,500-600"
        result = find_invalid_id_sum(data)
        expected = 111 + 1212 + 555
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
