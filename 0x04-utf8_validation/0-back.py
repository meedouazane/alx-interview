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
            if data[i] & 0b11000000 == 0b11000000:
                if not ((data[i + 1]) & 0b11000000 == 0b10000000
                        and (data[i + 2]) & 0b11000000 == 0b10000000):
                    return False
                i += 2
            elif (data[i]) & 0b11100000 == 0b11100000:
                if not ((data[i + 1]) & 0b11000000 == 0b10000000 and
                        (data[i + 2]) & 0b11000000 == 0b10000000 and
                        (data[i + 3]) & 0b11000000 == 0b10000000):
                    return False
                i += 3
            elif data[i] & 0b11110000 == 0b11110000:
                if not (data[i + 1] & 0b11000000 == 0b10000000 and
                        data[i + 2] & 0b11000000 == 0b10000000 and
                        data[i + 3] & 0b11000000 == 0b10000000 and
                        data[i + 4] & 0b11000000 == 0b10000000):
                    return False
                i += 4
            else:
                i += 1
        except IndexError:
            return False
    return True
