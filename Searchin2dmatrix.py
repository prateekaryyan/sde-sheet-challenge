from os import *
from sys import *
from collections import *
from math import *


def findTargetInMatrix(mat, m, n, target):
    # Write your code here.
    
    start,end=0,m-1
    while start <= end:

        mid=(start+end)//2
        if target>mat[mid][0]:
            start+=1
        elif target<mat[mid][0]:
            end-=1
        else:
            return True
            break
    mid=end
    start=0
    end=n-1
 
    while start<=end:
        midcol=(start+end)//2
        if target>mat[mid][midcol]:
            start+=1
        elif target<mat[mid][midcol]:
            end-=1
        else:
            return True
    return False