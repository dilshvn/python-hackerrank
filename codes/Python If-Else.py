#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input(""))
    if (n%2)==0:
        if (2<=n<=5)==1:
            print ("Not Weird")
        elif (6<=n<=20)==1:
            print ("Weird")
        elif (n>20)==1:
            print ("Not Weird")
    else:
        print ("Weird")
            
