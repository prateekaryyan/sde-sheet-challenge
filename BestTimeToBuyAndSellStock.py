from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(prices):
    # Write your code here.
    buy=prices[0]
    sell=prices[0]
    profit=buy-sell
    for i in range(1,len(prices)):
        if prices[i]<buy:
            buy=prices[i]
        elif prices[i]>buy:
            sell=prices[i]
            profit=max(profit,sell-buy)
    return profit        