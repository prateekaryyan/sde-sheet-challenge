from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit

class Solution:
    def __init__ (self, start, end):
        self.start = start
        self.end = end

def mergeIntervals(intervals):
    # Write your code here.
        intervals=sorted(intervals,key=lambda y:y.start)
        def merger(a,b):
            x1,y1=a.start,a.end
            x2,y2=b.start,b.end
            mi=min(x1,x2)
            ma=max(y1,y2)
            if y1>=x2:
                return [Solution(mi,ma)]
            else:
                return [a,b]

                
        a=intervals.pop(0)
        ans=[a]
        while intervals:
            b=intervals.pop(0)
            c=merger(ans.pop(),b)
            ans.extend(c)
        return ans
    

n = int(input())
arr1 = list(map(int, stdin.readline().strip().split(" ")))
arr2 = list(map(int, stdin.readline().strip().split(" ")))
arr1.sort()
arr2.sort()
intervals = []
for i in range(n):
    a = Solution(arr1[i], arr2[i])
    intervals.append(a)

res = mergeIntervals(intervals)

for i in range(len(res)):
    print(res[i].start, res[i].end)
