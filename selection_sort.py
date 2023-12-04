def smallest(li):
    s=li[0]
    l=len(li)
    index=0
    for i in range(1,l):
        if s<li[i]:
            s=li[i]
            index=i
    return (s,index)

if "__main__"==__name__:
    a=[34,56,23,45,2,456]
    c=[]
    le=len(a)
    while le!=0:
        value,ind=smallest(a)
        print("value",value,"index",ind)
        a.pop(ind)
        le-=1
        c.append(value)
    print(c)
        
