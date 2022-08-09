from itertools import combinations_with_replacement
a=list(map(str,input().split()))
s=list(combinations_with_replacement(a[0],int(a[1])))
for i in range(len(s)):
    s[i]=sorted(s[i])
for i in sorted(s):
    print("".join(i))
