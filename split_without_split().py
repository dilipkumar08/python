s='a;b;c;f'
a=[]
t=''
if s[len(s)-1]!=";":
    s=s+";"
for i in s:
    if i!=";":
        t=t+i
    a.append(t)
    print(t)
    t=''
    

    
        
    
