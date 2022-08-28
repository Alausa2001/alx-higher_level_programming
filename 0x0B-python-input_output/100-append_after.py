#!/usr/bin/python3
"""contains a function that appends a file after it searches for
a certian string"""


def append_after(filename="", search_string="", new_string=""):
    """appends the file with ``search_string`` is a substring of a
    line in the file. The string is appended just after the line which
    ``search_string`` is a substring of"""
    lines = []
    with open(filename, 'r+', encoding='utf-8') as f:
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)
