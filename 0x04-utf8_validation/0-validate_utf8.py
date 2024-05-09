#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    UTF-8 Validation
    :param data: data set (can contain multiple characters)
    :return: True if data is a valid UTF-8 encoding, else return False
    """
    i = 0
    while i < len(data):
        try:
            if (data[i] & 0b10000000) == 0:
                i += 1
            elif (data[i] & 0b11100000) == 0b11000000:
                if (data[i + 1] & 0b11000000) != 0b10000000:
                    return False
                i += 2
            elif (data[i] & 0b11110000) == 0b11100000:
                if (data[i + 1] & 0b11000000) != 0b10000000 or \
                   (data[i + 2] & 0b11000000) != 0b10000000:
                    return False
                i += 3
            elif (data[i] & 0b11111000) == 0b11110000:
                if (data[i + 1] & 0b11000000) != 0b10000000 or \
                   (data[i + 2] & 0b11000000) != 0b10000000 or \
                   (data[i + 3] & 0b11000000) != 0b10000000:
                    return False
                i += 4
            else:
                return False
        except IndexError:
            return False
    return True
