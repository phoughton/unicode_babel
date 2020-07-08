import unittest
from unicode_babel import tools, filters


class TestUnicodeFiltersOutNamed(unittest.TestCase):

    def test__filter_in_non_named_codepoints(self):
        code_points_with_no_names = [0x098D, 0x1FF0, 0x1F16, 0x2D26, 0x008E, 0x0000]
        for code_point in code_points_with_no_names:
            self.assertNotEqual(None, filters.filter_in_if_no_name(chr(code_point)), "They have no name so should not return None")

    def test__filter_out_named_codepoints(self):
        code_points_with_names = [0x2D00, 0x10805]
        for code_point in code_points_with_names:
            self.assertEqual(None, filters.filter_in_if_no_name(chr(code_point)), f"They have  names so should return None (Code point: {code_point})")

    def test__check_filter_barfs_when_passed_valid_codepoint(self):
        self.assertRaises(TypeError, filters.filter_in_if_no_name, chr(0x2D00), "Named codepoint should return TypeError")


if __name__ == '__main__':
    unittest.main()
