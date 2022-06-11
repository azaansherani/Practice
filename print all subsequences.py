def printSubseq(index , res, arr):
    if index == len(arr):
        print(res)
        return
    
    #take or pick the particular index into the subsequence
    printSubseq(index+1, res+[arr[index]], arr)

    #not pick or not take condition, element is not added to your subsequence

    printSubseq(index+1, res, arr)

    return
    
arr = [3,1,2]
printSubseq(0,[],arr)

#TC : 2^n * n(if you're using for loop to print array)
#SC : O(n), here max recursion depth is 3 cuz max 3 recursive calls k baad index n hojaata h
#[3, 1, 2]
#can also do it in the reverse order, in which first all the non take/pick calls will be made the the take ones