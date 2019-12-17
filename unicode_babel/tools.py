import random

# https://en.wikipedia.org/wiki/Unicode

planes = {
    0: [
        (0x0000, 0x10000)
    ]
    ,
    1: [
        (0x10000, 0x15000),
        (0x16000, 0x19000),
        (0x1B000, 0x1C000),
        (0x1D000, 0x20000)
    ]
    ,
    2: [
        (0x20000, 0x30000)
    ]
}


class CodePointGenerator:

    def __init__(self, planes_to_use=None):
        self._codepoint_range = self.build_codepoint_range(planes_to_use)
        self._codepoints_chosen = []

    @staticmethod
    def build_codepoint_range(planes_to_use=None):

        ranges_to_add = []

        if planes_to_use is None:
            planes_to_use = [0]

        for plane_id in planes_to_use:
            for each_range in planes[plane_id]:
                ranges_to_add.append(each_range)

        complete_list_of_choices = []

        for each_range in ranges_to_add:
            complete_list_of_choices.extend(list(range(*each_range)))

        return complete_list_of_choices

    def get_random_codepoint(self, filter_with_this=None):
        if filter_with_this is None:
            chosen_codepoint = chr(random.choice(self._codepoint_range))
            self._codepoints_chosen.append(chosen_codepoint)
            return chosen_codepoint
        else:
            chosen_codepoint = None
            while chosen_codepoint is None:
                chosen_codepoint = filter_with_this(self.get_random_codepoint())

            self._codepoints_chosen.append(chosen_codepoint)
            return chosen_codepoint

    def random_codepoints(self, number_needed, filter_with_this=None):
        for item in range(number_needed):
            yield self.get_random_codepoint(filter_with_this)

