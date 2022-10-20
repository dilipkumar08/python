
#Method-1 (Without Helper function)


def hasConsecutiveRepeat(string):
    res=False
    if len(string)>1:
        if string[0]!=string[1]:
            string=string[1:]
            res=hasConsecutiveRepeat(string)
        else:
            string=""
            return True
    return res
print(hasConsecutiveRepeat(string=str(input())))


#Method-2 (With Helper function)

def hasConsecutiveRepeat(string,l):
    res=False
    if l-2>=0:
        if string[l-2]!=string[l-1]:
            res=hasConsecutiveRepeat(string,l-1)
        else:
            return True
    return res
string=str(input("Enter the string: "))
l=len(string) #helper function 
print(hasConsecutiveRepeat(string,l))
