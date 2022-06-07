from os import *
from sys import *
from collections import *
from math import *


def findMajorityElement(arr, n):
	# Write your code here.
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in d:
        if d[i]>n//2:
            return i
    return -1

