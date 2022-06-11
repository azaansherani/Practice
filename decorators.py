def dec1(func1):
    def nowExec(a,b):
        print("Executing")
        func1(a,b)
        print("Executed")
    return nowExec

@dec1
def sum1(a,b):
    print(a+b)

sum1(10213,3102)