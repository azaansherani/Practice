def decrement_list(lst):
    lst2 = list(map(lambda x: x-1, lst))
    return lst2

print(decrement_list([1,2,3,4,5,6,7,8]))