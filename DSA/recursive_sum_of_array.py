def sumup(arr):
    if arr:
        return arr.pop()+sumup(arr)
    else:
        return 0
if __name__=="__main__":
    arr=[1,2,3,4,6,5,4,2,1]
    print('sum of the elements in the given array:',sumup(arr))
