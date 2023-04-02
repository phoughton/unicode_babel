import random

"""This module generates random Unicode codepoints based on specific Unicode planes. The planes dictionary contains
he valid ranges for each Unicode plane. The CodePointGenerator class creates random codepoints using the specified
planes.

Attributes:
    planes (dict): A dictionary containing the valid Unicode codepoint ranges for each Unicode plane.

Classes:
    CodePointGenerator: A class to generate random Unicode codepoints based on specific Unicode planes.

Methods:
    __init__(self, planes_to_use=None):
        Initializes a new instance of the CodePointGenerator class.

    build_codepoint_range(planes_to_use=None):
        Builds the codepoint range list based on the specified planes.

    get_random_codepoint(self, filter_with_this=None):
        Returns a random codepoint from the specified planes,
        filtered by an optional filter function.

    random_codepoints(self, number_needed, filter_with_this=None):
        A generator method that yields the specified
        number of random codepoints, filtered by an optional filter function.

"""

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
    """A class to generate random Unicode codepoints based on specific Unicode planes.

    Attributes:
        _codepoint_range (list): The list of valid codepoints based on the specified Unicode planes.
        _codepoints_chosen (list): The list of codepoints that have been chosen.
    """

    def __init__(self, planes_to_use=None):
        """Initializes a new instance of the CodePointGenerator class.

        Args:
            planes_to_use (list, optional): A list of integers representing the Unicode planes to use.
                Defaults to None, which uses only the first Unicode plane (Basic Multilingual Plane).
        """

        self._codepoint_range = self.build_codepoint_range(planes_to_use)
        self._codepoints_chosen = []

    @staticmethod
    def build_codepoint_range(planes_to_use=None):
        """Builds the codepoint range list based on the specified planes.

        Args:
            planes_to_use (list, optional): A list of integers representing the Unicode planes to use.
                Defaults to None, which uses only the first Unicode plane (Basic Multilingual Plane).

        Returns:
            list: The list of valid codepoints based on the specified Unicode planes.
        """

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
        """Returns a random codepoint from the specified planes, filtered by an optional filter function.

        Args:
            filter_with_this (callable, optional): A filter function to apply on the generated codepoints.
                Defaults to None, which doesn't apply any filter.

        Returns:
            str: A randomly chosen Unicode codepoint from the specified planes, filtered by the given filter function.
        """

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
        """A generator method that yields the specified number of random codepoints, filtered by an optional filter function.

        Args:
            number_needed (int): The number of random codepoints to generate.
            filter_with_this (callable, optional): A filter function to apply on the generated codepoints.
                Defaults to None, which doesn't apply any filter.

        Yields:
            str: A randomly chosen Unicode codepoint from the specified planes, filtered by the given filter function.
        """
        
        for item in range(number_needed):
            yield self.get_random_codepoint(filter_with_this)

