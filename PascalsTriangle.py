from os import *
from re import A
from sys import *
from collections import *
from math import *

#throwing some compiler issue
def printPascal(n:int):
    # Write your code here.
    # Return a list of lists.
    a=[[1]]
    
    for i in range(1,n+1):
        b=a[-1]
        c=[1]
        for i in range(len(b)-1):
            c.append(b[i]+b[i+1])
        c.append(1)
        a.append(c)
    return a


print(printPascal(4))