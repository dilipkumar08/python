s=str(input())

lcu,lc,ls=0,0,0
res=''
for i in s:
    if i==')':
        if lc==0:
            res='no'
            break
        else:
            lc-=1
    elif i=='(':
        lc+=1
    elif i=='}':
        if lcu==0:
            res='no'
            break
        else:
            lcu-=1
    elif i=='{':
        lcu+=1
    elif i==']':
        if ls==0:
            res='no'
            break
        else:
            ls-=1
    elif i=='[':
        ls+=1


if not res:
    if not lcu and not lc and not ls:
        print('yes')
    else:
        print('no')
else:
    print(res)
