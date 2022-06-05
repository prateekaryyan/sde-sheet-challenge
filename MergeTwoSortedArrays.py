from os import *
from sys import *
from collections import *
from math import *

def ninjaAndSortedArrays(arr1,arr2,m,n):
    # Write your code here.
       i,j=0,0
       ans=[]
       while i<m and j<n:
           if arr1[i]<=arr2[j]:
                ans.append(arr1[i])
                i+=1
           else:
                ans.append(arr2[j])
                j+=1
       
       while i<m:
            ans.append(arr1[i])
            i+=1
       while j<n:
           ans.append(arr2[j])
           j+=1
       return ans
