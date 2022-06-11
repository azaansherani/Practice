def binarySearch(lst,numf):
    lindex = 0
    rindex = len(lst)-1

    while lindex<=rindex:
        mid = lindex + (rindex-lindex)//2
        
        if numf==lst[mid]:
            return mid
        elif numf<lst[mid]:
            rindex = mid-1
        else:
            lindex = mid+1
    return -1
# better approach
# if numf<lst[mid]:                            
#             rindex = mid-1
#         else:
#             lindex = mid+1
#     return rindex

def countOccurences(lst,nuf,index):
    count = 1
    lmost = 0
    rmost = 0
    i=0
    while i<index:
        if lst[i]==nuf:
            count=count+1
            if lmost==0:
                lmost = i
        i = i+1
    i = len(lst)-1

    while i>index:
        if lst[i]==nuf:
            count=count+1
            if rmost==0:
                rmost = i
        i = i-1
    
    print(f"Index: {index}, Coutn: {count}, First Occurence: {lmost}, Last Occurence: {rmost}")

if __name__ == "__main__":
    lst = [12,43,45,65,76,87,90,99]
    numf = 99


    index = binarySearch(lst,numf)
    #countOccurences(lst,numf,index)
    print(index)
