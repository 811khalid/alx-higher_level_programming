#!/usr/bin/python3
"""
Module docs
"""


def append_write(filename="", text=""):
    """
    function docs
    """
    with open(filename, "a", encoding="utf-8") as f:
        num = f.write(text)
    return num
