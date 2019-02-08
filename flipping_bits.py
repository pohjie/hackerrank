#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    bits = [0] * 32
    
    # convert input to bit representation first
    for i in range(32):
        if (2 ** (31 - i) <= n):
            bits[i] = 1
            n = n - 2 ** (31 - i)

    # calculate value of flipped bits
    ans = 0
    for i in range(32):
        if bits[i] == 0: # flipped
            ans = ans + 2 ** (31 - i)

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
