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
    
#to print the split values without storing them

d=""
string='ade;gjgi;fdf'
for i in string:
    if i==";":
        print(d)
        d=""
    else:
        d=d+i
print(d)   
