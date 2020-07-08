import unicodedata


def filter_out_if_no_name(the_codepoint):
    try:
        unicodedata.name(the_codepoint)
    except ValueError:
        return None

    return the_codepoint


def filter_out_if_no_name_unless_latin_control_char(the_codepoint):
    if ord(the_codepoint) <= 0x0FF:
        return the_codepoint
    else:
        return filter_out_if_no_name(the_codepoint)


def filter_in_if_no_name(the_codepoint):
    try:
        unicodedata.name(the_codepoint)
    except ValueError:
        return the_codepoint

    return None
