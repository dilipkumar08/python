def sortedSquaredArray(array):
    array=sorted(array,reverse=False)
    l=len(array)
    for i in range(l):
        array[i]=array[i]**2
    return(sorted(array))
array=[2,5,4,7,6,8]
print(sortedSquaredArray(array))
