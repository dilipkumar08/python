N=int(input())
for i in range(N):
    s=str(input())
    temp=0
    if s=="0" or s[-1]==".":
            print("False")
    else:
        try:
            temp=float(s)
            print("True")
        except:
            print("False")
