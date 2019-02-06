#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximizingXor function below.
def maximizingXor(l, r):
    max_val = 0

    for pair_left in range(l, r+1):
        for pair_right in range(pair_left, r+1):
            xor_val = pair_left ^ pair_right

            if xor_val > max_val:
                max_val = xor_val

    return max_val



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
