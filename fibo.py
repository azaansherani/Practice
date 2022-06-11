# def fibo(n,dp):
#     if dp[n]!=-1:
#         return dp[n]
#     if n<=1:
#         return n
#     dp[n] = fibo(n-1,dp)+fibo(n-2,dp)
#     return(dp[n])
# n=11
# dp=[-1]*(n+1)
# print(fibo(n,dp)) 

# def fibo(n):
#     a,b=0,1
#     if n<=1:
#         return n
#     for i in range(n-2):
#         b=b+a
#         a=b-a
#     return b+a
    
def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)

n = 2
print(fibo(n))