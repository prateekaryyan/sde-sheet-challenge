from os import *
from sys import *
from collections import *
from math import *

def majorityElementII(arr):
    # Write your code here.
    d={}
    n=len(arr)
    ans=[]
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in d:
        if d[i]>n//3:
            ans.append(i)
    return ans