def isValidSubsequence(array, sequence):
    a=len(sequence)
    b=len(array)
    n=0
    if a<=b:
        for i in sequence:
            c=len(array)
            if i in array[n:c]:
                result= True
                n=array.index(i)
                array.remove(i)
               
            else:
                result=False
                break;
    else:
        result=False
    return(result)
    

array=[5, 1, 22, 25, 6, -1, 8, 10]
sequence=[5, 1, 22, 6, -1, 8, 10]
print(isValidSubsequence(array, sequence))
