def sameElements(list1:list[int],list2:list[int],index=0):
    if index==0:
        l1=len(list1)
        l2=len(list2)
        if l1==l2:
            list1.sort()
            list2.sort()
        else:
            return False
    try:
        if list1[index]==list2[index]:
            return sameElements(list1,list2,index=index+1)
        else:
            return False
    except:
        if l1==0 and l2==0:
            return  "The list is Empty"
        else:
            return True
    
    
