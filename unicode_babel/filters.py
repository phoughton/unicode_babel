import unicodedata


def filter_out_if_no_name(the_codepoint):
    try:
        unicodedata.name(the_codepoint)
    except ValueError:
        return None

    return the_codepoint

