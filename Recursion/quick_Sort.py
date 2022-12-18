def qs(li):
    if len(li)<2:
        return li
    elif len(li)==2:
        if li[0]>li[1]:
            return [li[1],li[0]]
        else:
            return li
    else:
        temp=li[0]
        less=[i for i in li[1:] if i<=temp]
        great=[j for j in li[1:] if j>temp]
        return qs(less)+[temp]+qs(great)
        
        return +qs(li[:])
qs([10,1,12,23,1,4,5,4,2])
