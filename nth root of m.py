def findNthRootOfM(n,m):
    # Write your Code here.
    left = 1.000000
    right = m/(n-1)
    sp = 1e-7
    while right-left>sp:
        mid = (left + right)/2.0
        if mid**n<m:
            left = mid
        else:
            right = mid
    return format(right,'.6f')

n = 3
m = 2
print(findNthRootOfM(n,m))