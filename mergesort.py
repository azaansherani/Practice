def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)

def merge_two_sorted_lists(a,b,arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1

    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1

    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1

if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

    for arr in test_cases:
        merge_sort(arr)
        print(arr)



"""
https://github.com/codebasics/data-structures-algorithms-python/blob/master/algorithms/5_MergeSort/merge_sort_exercise.md
"""

def merge_sorted_arrays(a,b,arr,key):
    i = j = k = 0
    while i<len(a) and j<len(b):
        if a[i][key]<=b[j][key]:
            arr[k]=a[i]
            i+=1
        else:
            arr[k]=b[j]
            j+=1
        k+=1
    while i<len(a):
        arr[k]=a[i]
        i+=1
        k+=1
    while j<len(b):
        arr[k]=b[j]
        j+=1
        k+=1
        

def merge_sort(elements, key='time_hours', descending=False):
    if len(elements)<=1:
        return
    mid = len(elements)//2
    left = elements[:mid]
    right = elements[mid:]

    merge_sort(left,key)
    merge_sort(right,key)

    merge_sorted_arrays(left,right,elements,key)
    if descending==True:
        elements.reverse()
# elements[::-1] = elements works, elements[:]=elements[::-1] also works




if __name__ == "__main__":
    elements = [
        { 'name': 'vlad',   'age': 17, 'time_hours': 1},
        { 'name': 'zlatan', 'age': 12,  'time_hours': 3},
        { 'name': 'elon',  'age': 21,  'time_hours': 2.5},
        { 'name': 'akshay',  'age': 24,  'time_hours': 1.5},
    ]
    merge_sort(elements, 'age', True)
    print(elements)
