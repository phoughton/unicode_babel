import unittest
from unicode_babel import tools, filters


class TestCombined(unittest.TestCase):

    def test_get_codepoint_filter_out_unnamed_plane_0(self):
        genny = tools.CodePointGenerator([0])
        gen_char = genny.get_random_codepoint(filters.filter_out_if_no_name)
        self.assertEqual(1, len(gen_char), "filter out unnamed plane 0")

    def test_get_codepoint_filter_out_unnamed_plane_1(self):
        genny = tools.CodePointGenerator([1])
        gen_char = genny.get_random_codepoint(filters.filter_out_if_no_name)
        self.assertEqual(1, len(gen_char), "filter out unnamed plane 1")

    def test_get_codepoint_filter_out_iterator_plane_0(self):
        codepoint_list = self.build_codepoint_list([0], filters.filter_out_if_no_name, 10)
        self.assertEqual(10, len(codepoint_list), "iterator of 10")

    def test_get_codepoint_filter_out_iterator_planes_0_1(self):
        codepoint_list = self.build_codepoint_list([0, 1], filters.filter_out_if_no_name, 10)
        self.assertEqual(10, len(codepoint_list), "iterator of 10")

    def test_get_codepoint_filter_out_iterator_planes_0_1_2(self):
        codepoint_list = self.build_codepoint_list([0, 1, 2], filters.filter_out_if_no_name, 10)
        self.assertEqual(10, len(codepoint_list), "iterator of 10")

    def test_get_codepoint_filter_out_iterator_planes_1_2(self):
        codepoint_list = self.build_codepoint_list([1, 2], filters.filter_out_if_no_name, 10)
        self.assertEqual(10, len(codepoint_list), "iterator of 10")

    @staticmethod
    def build_codepoint_list(planes: list, codepoint_filter, expectation: int):
        genny = tools.CodePointGenerator(planes)
        codepoint_list = []
        for point in genny.random_codepoints(10, codepoint_filter):
            codepoint_list.append(point)
        return codepoint_list


if __name__ == '__main__':
    unittest.main()
