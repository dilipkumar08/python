a=[1,2,3,4,5,6,7,8,10,12,13,14,15,16,20]
target=20
def binary_search(li,target=0,index=0):
    if li[len(li)//2]>target:
        index+=1
        return binary_search(li[:(len(li)//2)-1],target,)
    elif li[(len(li)//2)]<target:
        index+=1
        return binary_search(li[(len(li)//2)+1:],target,index)
    else:
        return li[len(li)//2],index
binary_search(a,target)
