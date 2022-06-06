from os import *
from sys import *
from collections import *
from math import *

#somecompilerissue


def findDuplicate(arr:list, n:int):
    # Write your code here.
    # Returns an integer.
    d=set()

    for i in arr:
        if i in d:
#             print(i)
            return int(i)
        else: 
            d.add(i)
    return -1