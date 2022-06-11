a = [[1,2,3],[4,5,6],[7,8,9]]
lst=[]
for j in range(len(a)):
    lst1=[]
    for i in range(len(a)-1,-1,-1):
        lst1.append(a[i][j])
    lst.append(lst1)
print(lst)


"""
optimized solution
"""
n = len(a)
for i in range(n):
    for j in range(i):
        a[i][j],a[j][i]=a[j][i],a[i][j]#transpose
for i in range(n):
    for j in range(n//2):
        a[i][j],a[i][n-1-j]=a[i][n-1-j],a[i][j]
        