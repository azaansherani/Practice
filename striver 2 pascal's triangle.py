numRows=5
lstfinal = []
for i in range(numRows):
    lst = []
    for j in range(i+1):
        if j==0 or j==i:
            lst.append(1)
        else:
            lst.append(lstfinal[i-1][j-1]+lstfinal[i-1][j])
    lstfinal.append(lst)
print(lstfinal)