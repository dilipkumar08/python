l=[]
u=[]
t=int(input())
for j in range(t):
    s=str(input())
    for i in s:
        if i ==i.lower():
            l.append(i)
        elif i==i.upper():
            u.append(i)
    if len(l)>len(u):
        print("-1")
    elif len(l)<len(u):
        print("1")
    elif len(l)==len(u):
        print("0")
