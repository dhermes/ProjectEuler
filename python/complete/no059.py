#!/usr/bin/env python

from python.decorators import euler_timer
from python.functions import get_data


def translate(message, key):
    len_key = len(key)
    result = message[:]

    for i in range(len_key):
        for j in range(i, len(result), len_key):
            result[j] = result[j] ^ key[i]

    result = ''.join(chr(val) for val in result)
    return result


def main(verbose=False):
    message = get_data(59).split(',')

    message = [int(char) for char in message]

    possible_keys = []
    for ascii1 in range(97, 123):
        for ascii2 in range(97, 123):
            for ascii3 in range(97, 123):
                possible_keys.append([ascii1, ascii2, ascii3])

    for key in possible_keys:
        curr = translate(message, key)
        if (curr.upper().find('THE') != -1
            and curr.upper().find('IS') != -1
            and curr.upper().find('AND') != -1
            and curr.upper().find('OF') != -1
            and curr.upper().find('ARE') != -1):
            break

    key_as_word = ''.join(chr(val) for val in key)
    result = '\n\nActual Message:\n%s\n\nThe key is: %s or %s.' % (
        curr, key_as_word, key)

    if verbose:
        return '%s%s' % (sum(ord(letter) for letter in curr), result)
    else:
        return sum(ord(letter) for letter in curr)

if __name__ == '__main__':
    print euler_timer(59)(main)(verbose=True)
