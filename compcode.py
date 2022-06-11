import sys
from sys import stdin, stdout
from math import sqrt,gcd
from collections import deque
sys.setrecursionlimit(10**8)
ip = lambda :stdin.readline()
I     = lambda :int(ip())
S     = lambda :ip().strip()
M     = lambda :map(int,ip().strip().split())
L     = lambda :list(map(int,ip().strip().split()))
mod=1000000007


def atLeastMmetres(m, minWood):
    totalWood = 0
    for h in arr:
        wood = max(0,h-m)
        totalWood += wood
    return totalWood>=minWood

n, minWood = M()
arr = L()


l = 0
r = max(arr)
while l<=r:
    m = l + (r-l)//2  #height of saw blade
    if atLeastMmetres(m, minWood):
        ans = m
        l = m+1
    else:
        r = m-1
print(ans)

    

