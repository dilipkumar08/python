def smallest(li):
    small=li[0]
    index=0
    for i in range(1,len(li)):
        if small>li[i]:
            small=li[i]
            index=i
    return small,index
def sort_list(li): #li is the list to be sorted
    for  i in range(len(li)):
        val,index=smallest(li[i:])
        li.pop(index+i)
        li.insert(i,val)

sort_list(li) #passing the list to the function
    
