#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a_dict = {}
    b_dict = {}

    for character in a:
        if character in a_dict:
            a_dict[character] = a_dict[character] + 1
        else:
            a_dict[character] = 1

    for character in b:
        if character in b_dict:
            b_dict[character] = b_dict[character] + 1
        else:
            b_dict[character] = 1

    dictionaries = [a_dict, b_dict]
    if len(a_dict) >= len(b_dict):
        idx = 0
        other_idx = 1
    else:
        idx = 1
        other_idx = 0

    num_removed = 0
    for index, (character, count) in enumerate(dictionaries[idx].items()):
        if character in dictionaries[other_idx]:
            num_removed = num_removed + abs(count - dictionaries[other_idx][character])
        else:
            num_removed = num_removed + count

    for index, (character, count) in enumerate(dictionaries[other_idx].items()):
        if character not in dictionaries[idx]:
            num_removed += count

    return num_removed
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
