import unittest
from unicode_babel import tools, filters


class TestUnicodeFiltersOutNoName(unittest.TestCase):

    def test__filter_out_non_named_codepoints(self):
        code_points_with_no_names = [0x098D, 0x1FF0, 0x1F16, 0x2D26, 0x008E, 0x0000]
        for code_point in code_points_with_no_names:
            self.assertEqual(None, filters.filter_out_if_no_name(chr(code_point)), "They have no name so should return None")

    def test__filter_in_named_codepoints(self):
        code_points_with_no_names = [0x2D00, 0x10805]
        for code_point in code_points_with_no_names:
            self.assertNotEqual(None, filters.filter_out_if_no_name(chr(code_point)), f"They have names so should return not None (Code point: {code_point})")

    def test__check_filter_barfs_when_passed_none(self):
        self.assertRaises(TypeError, filters.filter_out_if_no_name, None, "None (e.g.: ununamed codepoint) should return TypeError")


if __name__ == '__main__':
    unittest.main()
