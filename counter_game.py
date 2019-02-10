#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the counterGame function below.
def counterGame(n):
    if n == 1:
        return ("Richard")

    powers_of_two = [0] * 64
    for i in range(64):
        powers_of_two[i] = 2 ** i

    # let Louise's win be denoted by odd numbers, and Richard's by even
    turn_num = 0
    while (n != 1):
        if (n in powers_of_two):
            n = n / 2
        else:
            for val in reversed(powers_of_two):
                if val < n:
                    n = n - val
                    break
        
        turn_num = turn_num + 1

    if turn_num % 2 == 0:
        return("Richard")
    else:
        return("Louise")



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
