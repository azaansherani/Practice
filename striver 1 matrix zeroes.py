matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(matrix)
rowlen = len(matrix)
colen = len(matrix[0])

colvar=True

for i in range(rowlen):
    if matrix[i][0]==0:
        colvar=False
    for j in range(1,colen):
        if matrix[i][j]==0:
            matrix[i][0]=matrix[0][j]=0

for i in range(rowlen-1,-1,-1):
    for j in range(colen-1,0,-1):
        if matrix[i][0]==0 or matrix[0][j]==0:
            matrix[i][j]=0
    if colvar == False:
        matrix[i][0]=0


print(matrix)





















# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# print(matrix)
# rowlen = len(matrix)
# colen = len(matrix[0])

# colarr=[-6969]*colen
# rowarr=[-6969]*rowlen

# for i in range(rowlen):
#     for j in range(colen):
#         if matrix[i][j]==0:
#             rowarr[i]=0
#             colarr[j]=0
# for i in range(rowlen):
#     for j in range(colen):
#         if rowarr[i]==0 or colarr[j]==0:
#             matrix[i][j]=0
# print(matrix)