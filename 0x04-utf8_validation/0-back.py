#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    UTF-8 Validation
    :param data: data set (can contain multiple characters)
    :return: True if data is a valid UTF-8 encoding, else return False
    """
    for i in data:
        if i > 255 or i < 0:
            return False
    return True
