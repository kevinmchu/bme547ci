'''
is_tachycardic.py
Author: Kevin Chu
Last Modified: 2/4/19

DESCRIPTION: This program takes a string as an input and determines whether
it contains the word "tachycardic".
'''
import re


def is_tachycardic(test_str):
    # Make all characters lowercase
    test_str = test_str.lower()

    # By default, isTachycardic is false
    # If string contains "tachycardic," then change to true
    isTachycardic = False

    # Check to see if now lowercase string contains tachycardic
    if test_str.find("tachycardic") != -1:
        isTachycardic = True

    return isTachycardic
