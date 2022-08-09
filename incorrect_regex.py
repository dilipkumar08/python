import re
a=""
n=int(input())
for i in range(n):
    r=str(input())
    try:
        s=re.search(r,a)
        if s==None:
            print("True")
    except:
        print("False")
            
