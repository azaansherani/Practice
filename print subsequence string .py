def subseq(index, res, s):
    if index>=len(s):
        print(res)
        return
    
    #take
    subseq(index+1, res + s[index], s)

    #not take
    subseq(index+1, res, s)

    
s = 'rad'
subseq(0,'', s)
