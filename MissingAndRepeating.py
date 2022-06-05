from os import *
from sys import *
from collections import *
from math import *

def missingAndRepeating(arr, n):
    # Write your code her
    d=set()
    repeat=None
    for i in arr:
        if i in d:
            repeat=i
            break
        else:
            d.add(i)
    
    missing = sum(range(1,n+1))-(sum(arr)-repeat)
#     print(repeat,missing)
    return (missing,repeat)