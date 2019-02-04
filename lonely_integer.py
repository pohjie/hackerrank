#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the lonelyinteger function below.
def lonelyinteger(a):
    val2place = {}
    place2val = {}
    idx = 0

    on_off = [0] * len(a)

    for i in range(len(a)):
        val = a[i]
        if val in val2place:
            place = val2place[val]
        else:
            val2place[val] = idx
            place2val[idx] = val
            place = idx
            idx = idx + 1

        on_off[place] = on_off[place] ^ 1

    for i in range(len(on_off)):
        if on_off[i] == 1:
            return place2val[i]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
