#Method-1
def digitalRoot(n:int):
    if n>9:
        res=0
        while True:
            res=res+(n%10)
            n=n//10
            if n==0:
                break
        n=digitalRoot(n=res)
    return n

#-----------------------------------------------------------------------------------------------------------------------------------
#Method-2

def digitalRoot(n:int,res=0):
    if n>9:
        for i in str(n):
            res=res+int(i)
        n=digitalRoot(n=res)
    return n

#---------------------------------------------------------------------------------------------------------------------------------------
#Method-3

def digitalRoot(n:int):
    if n>9:
        n=int(eval('+'.join(str(n))))
        n=digitalRoot(n)
    return n
