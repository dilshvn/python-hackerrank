#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    i = 0
    Positive = 0
    Negative = 0
    Zero = 0
    while i in range(len(arr)):
        if (arr[i] > 0):
            Positive += 1
            Positive = Positive
        elif (arr[i] <0):
            Negative += 1
            Negative = Negative
        else:
            Zero += 1
            Zero = Zero
        i += 1
    print ("{:.6f}".format(Positive/n))
    print ("{:.6f}".format(Negative/n))
    print ("{:.6f}".format(Zero/n))
    return 0

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
