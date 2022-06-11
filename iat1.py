p = int(input())
q = int(input())
r = int(input())
x=0
no5=0
no1=0
if (p*5+q)<r :
	print(-1)
	exit()
else:
	while (x<r and no5<=p):
		x=x+5
		no5=no5+1 
	no1=r-(no5-1)*5
	print(no5-1)
	print(no1)	
