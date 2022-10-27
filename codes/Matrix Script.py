#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

pattern = r"(?<=\w)[!@#$%& ]{1,}(?=\s*\w)"

firstletter = ""

for col in range(m):
    for row in range(n):
        firstletter += str(matrix[row][col])

print(re.sub(pattern, " ", firstletter))
