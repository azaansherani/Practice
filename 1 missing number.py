a = [3,1,2,4,5]
n = len(a)+1
result = 0
for i in range(1,n+1):
    result = result^i

for i in a:
    result = result ^ i

print(result)