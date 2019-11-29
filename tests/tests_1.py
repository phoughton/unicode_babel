import unittest
from unicode_babel import tools, filters


class TestUnicodeGenerator(unittest.TestCase):

    def test_size_implicit_use_plane_0(self):
        self.assertEqual(65536, len(tools.CodePointGenerator.build_codepoint_range()), "Count codepoints in plane 0")

    def test_size_explicit_use_plane_0(self):
        self.assertEqual(65536, len(tools.CodePointGenerator.build_codepoint_range([0])), "Count codepoints in plane 1")

    def test_get_codepoint_no_filter_plane_1(self):
        genny = tools.CodePointGenerator([1])
        self.assertEqual(1, len(genny.get_random_codepoint()), "vanilla get codepoint may be unnamed")

    def test_get_codepoint_filter_out_unnamed_plane_0(self):
        genny = tools.CodePointGenerator([0])
        gen_char = genny.get_random_codepoint(filters.filter_out_if_no_name)
        self.assertEqual(1, len(gen_char), "filter out unnamed plane 0")

    def test_get_codepoint_filter_out_unnamed_plane_1(self):
        genny = tools.CodePointGenerator([1])
        gen_char = genny.get_random_codepoint(filters.filter_out_if_no_name)
        self.assertEqual(1, len(gen_char), "filter out unnamed plane 1")

    def test_get_codepoint_filter_out_iterator_plane_0(self):
        genny = tools.CodePointGenerator([0])
        codepoint_list = []
        for point in genny.random_codepoints(10, filters.filter_out_if_no_name):
            codepoint_list.append(point)
            self.assertEqual(1, len(point), "individual iteration item")

        self.assertEqual(10, len(codepoint_list), "iterator of 10")
        print(codepoint_list)

    def test_get_codepoint_filter_out_iterator_planes_0_1(self):
        genny = tools.CodePointGenerator([0, 1])
        codepoint_list = []
        for point in genny.random_codepoints(10, filters.filter_out_if_no_name):
            codepoint_list.append(point)
            self.assertEqual(1, len(point), "individual iteration item")

        self.assertEqual(10, len(codepoint_list), "iterator of 10")
        print(codepoint_list)


if __name__ == '__main__':
    unittest.main()
