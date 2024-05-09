#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    i = 0
    while i < len(data):
        try:
            if (data[i] & 0b10000000) == 0:  # 1-byte character
                i += 1
            elif (data[i] & 0b11100000) == 0b11000000:  # 2-byte character
                if (data[i + 1] & 0b11000000) != 0b10000000:
                    return False
                i += 2
            elif (data[i] & 0b11110000) == 0b11100000:  # 3-byte character
                if (data[i + 1] & 0b11000000) != 0b10000000 or \
                   (data[i + 2] & 0b11000000) != 0b10000000:
                    return False
                i += 3
            elif (data[i] & 0b11111000) == 0b11110000:  # 4-byte character
                if (data[i + 1] & 0b11000000) != 0b10000000 or \
                   (data[i + 2] & 0b11000000) != 0b10000000 or \
                   (data[i + 3] & 0b11000000) != 0b10000000:
                    return False
                i += 4
            else:
                return False  # Invalid starting byte
        except IndexError:
            return False  # Incomplete UTF-8 sequence
    return True

