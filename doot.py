def finalSeq(c, n, cards):
    points = 0
    arr = []

    for i in range(n):
        if cards[i] in arr:
            points+=1
        
        else:
            if len(arr)<c:
                arr.append(cards[i])
            else:
                arr[0] = cards[i]

    print(*arr, sep=" ")
    print(points)

print(finalSeq(3, 10, [2, 3, 4, 2, 1, 3, 7, 5, 4, 3]))

