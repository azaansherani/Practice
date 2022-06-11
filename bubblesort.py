def bubblesort(arr):
    size=len(arr)
    for i in range(size-1):
        for j in range(size-1-i):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

    print(arr)


# def bubblesort(elements,key):
#     size=len(elements)
#     for i in range(size):
#         for j in range(size-1-i):
#             if elements[j][key]>elements[j+1][key]:
#                 temp = elements[j]
#                 elements[j]=elements[j+1]
#                 elements[j+1]=temp

#     print(elements)





if __name__ == "__main__":
    # elements = [
    #     { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    #     { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
    #     { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
    #     { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    # ]
    arr = [55, 30, 9, 8, 7, 6, 4, 2, 1]
    bubblesort(arr)