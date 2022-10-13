import numpy as np
def addOneToEverything(arr,l):
    if l>0:
        l-=1
        arr[l]=arr[l]+1
        addOneToEverything(arr,l)
    else:
        print("arr ->",arr)
#arr= [define your array here]
arr=np.array(arr) #just in case if it should be an array
l=len(arr)
addOneToEverything(arr,l)#'l' as helper Function
