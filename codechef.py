def solution(n,N):
    ans = []
    for i in range(n-1):
        cnt=1
        while  i<n-1 and N[i]^N[i+1]<0:
            cnt +=1
            i+=1
        ans.append(cnt)
    ans.append(1)
    print(*ans, sep = ' ')

solution(4, [1,2,3,4])
solution(4, [1,-5,1,-5])
solution(6, [-5,-1,-1,2,-2,-3])

