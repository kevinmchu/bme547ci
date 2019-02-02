'''
is_tachycardic.py
Author: Kevin Chu
Last Modified: 2/1/19

DESCRIPTION: This program takes a string as an input and determines whether
it contains the word "tachycardic".
'''


def is_tachycardic(test_str):
    # Make all characters lowercase
    test_str = test_str.lower()
    # Remove extra whitespace
    test_str = test_str.replace(' ', '')

    isTachycardic = False

    if test_str == "tachycardic":
        isTachycardic = True

    return isTachycardic
