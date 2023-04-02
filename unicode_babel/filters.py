import unicodedata

"""This module provides a set of filter functions for Unicode codepoints based on their names. It uses the unicodedata
module to check the names of the codepoints.

Functions:
filter_out_if_no_name(the_codepoint):
Filters out codepoints that don't have a name.

filter_out_if_no_name_unless_latin_control_char(the_codepoint):
    Filters out codepoints that don't have a name, unless they are Latin control characters (<= 0x0FF).

filter_in_if_no_name(the_codepoint):
    Filters in codepoints that don't have a name, and filters out the ones with a name.
"""


def filter_out_if_no_name(the_codepoint):
    """Filters out codepoints that don't have a name.

    Args:
        the_codepoint (str): A single Unicode character.

    Returns:
        str: The input codepoint if it has a name, otherwise None.
    """

    try:
        unicodedata.name(the_codepoint)
    except ValueError:
        return None

    return the_codepoint


def filter_out_if_no_name_unless_latin_control_char(the_codepoint):
    """Filters out codepoints that don't have a name, unless they are Latin control characters (<= 0x0FF).

    Args:
        the_codepoint (str): A single Unicode character.

    Returns:
        str: The input codepoint if it has a name or is a Latin control character, otherwise None.
    """
    if ord(the_codepoint) <= 0x0FF:
        return the_codepoint
    else:
        return filter_out_if_no_name(the_codepoint)


def filter_in_if_no_name(the_codepoint):
    """Filters in codepoints that don't have a name, and filters out the ones with a name.

    Args:
        the_codepoint (str): A single Unicode character.

    Returns:
        str: The input codepoint if it doesn't have a name, otherwise None.
    """
    try:
        unicodedata.name(the_codepoint)
    except ValueError:
        return the_codepoint

    return None
