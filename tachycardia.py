'''
is_tachycardic.py
Author: Kevin Chu
Last Modified: 2/1/19

DESCRIPTION: This program takes a string as an input and determines whether
it contains the word "tachycardic".
'''


def is_tachycardic(test_str):
    test_str = test_str.lower()

    isTachycardic = False

    if test_str == "tachycardic":
        isTachycardic = True

    return isTachycardic
