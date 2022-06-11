# def fibo(n):
#     if n<=1:
#         return n
#     else:
#         return fibo(n-1)+fibo(n-2)
# print(fibo(11))

# def fibo(n,dp): #using dp
#     if n<=1:
#         dp[n] = n
#     else:
#         dp[n] = fibo(n-1,dp) + fibo(n-2,dp)
#     return dp[n]
# n=11
# dp = [-1]*(n+1)
# print(fibo(n,dp))

# def checkPallindrome(i,strr,n): 
#     if i<n//2:
#         if strr[i] != strr[n-1-i]:
#             return False
#         return checkPallindrome(i+1,strr,n)
#     return True

#     if i>=n//2:
#         return True
#     if strr[i] != strr[n-1-i]:
#         return False
#     return checkPallindrome(i+1,strr,n)
# TC: O(n/2) SC: O(n/2) {stack space}

# strr = "radaar"
# bool = checkPallindrome(0,strr,len(strr))
# print(bool)

# def reverseArray(i,arr,n):
#     if i<n//2:
#         arr[i],arr[n-1-i] = arr[n-1-i],arr[i]
#         reverseArray(i+1,arr,n)

# arr = [1,2,3,4,5,6,7,8,9]
# reverseArray(0,arr,len(arr))
# print(arr)

# def reverseArray(i,arr,j):
#     if i<j:
#         arr[i],arr[j] = arr[j],arr[i]
#         reverseArray(i+1,arr,j-1)

# arr = [1,2,3,4,5,6,7,8,9]
# reverseArray(0,arr,len(arr)-1)
# print(arr)

#factorial of N, functional
# def fact(n):
#     if n == 1:
#         return 1
#     return n*fact(n-1)
# print(fact(5))

#parameterized
# def fact(n,fac): 
#     if n == 1:
#         print(fac)
#         return
#     fact(n-1,fac*n)
    
# fact(5,1)
    

#functional recursion
# def recur(n):
#     if n == 0:
#         return 0
#     return n + recur(n-1)

# print(recur(5))


#parameterized recursion
#  def sumN(n,sum):
#     if n == 0:
#         print(sum)
#         return
#     sumN(n-1,sum+n)
# sumN(5,0)

# backtrack
# def recur(n):
#     if n==0:
#         return
#     recur(n-1)
#     print(n)
# recur(5)

# def sumN(n, sum):
#     if n==0:
#         return
#     sum[0]+=n
#     sumN(n-1,sum)
# sum=[0]
# sumN(5,sum)
# print(sum[0])
