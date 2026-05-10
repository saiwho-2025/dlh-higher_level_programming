#!/usr/bin/python3
"""this module inserts a line of text to a file,
following a specific string at the labled lines"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing
    a specific string.

    Args:
        filename(str): The name of the file.
        search_string(str): The string to search for in each line.
        new_string(str): The string to insert after a match.
    """
    lines_to_write = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            lines_to_write.append(line)
            if search_string in line:
                lines_to_write.append(new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines_to_write)
