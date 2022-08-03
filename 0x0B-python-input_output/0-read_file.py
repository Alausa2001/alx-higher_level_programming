#!/usr/bin/python3
"""MODULE CONTAINS A FUNCTION THAT READS A FILE TO STDOUT"""


def read_file(filename=""):
    """READS A FILE TO STDOUT"""
    with open('UTF8', 'r', encoding='utf-8') as f:
        result = f.read()
        print(result)
