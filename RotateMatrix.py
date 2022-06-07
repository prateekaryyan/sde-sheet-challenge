from os import *
from sys import *
from collections import *
from math import *
a=[]

def rotateMatrix(matrix, n, m):
    r=c=0 
    while r<n//2  and c<m//2:
        
        i=r+1
        j=c+1
        prev=matrix[r][c]
        a=[]
        while j<m-r:
            a.append(matrix[r][j])
            temp=matrix[r][j]
            matrix[r][j]=prev
            prev=temp
            j+=1
        j-=1    
        while i<n-c:
            a.append(matrix[i][j])
            temp=matrix[i][j]
            matrix[i][j]=prev
            prev=temp
            i+=1
        i-=1
        j-=1
        while j>=c:
            temp=matrix[i][j]
            matrix[i][j]=prev
            prev=temp
            j-=1
        j+=1
        i-=1
        while i>=r:
            temp=matrix[i][j]
            matrix[i][j]=prev
            prev=temp
            i-=1

        r+=1
        c+=1

#     return matrix
        
    
    
        
    