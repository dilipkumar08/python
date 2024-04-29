inp=int(input())

L,R=map(int,input().split())

if L>R:
    if inp>=R and inp<=L:
        print('yes')
    else:
        print('no')
elif R>L:
    if inp>=L and inp<=R:
        print('yes')
    else:
        print('no')
elif R==L:
    if inp==R:
        print('yes')
    else:
        print('no')
