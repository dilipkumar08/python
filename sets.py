l = int(input())
s = set(map(int, input().split()))
n = int(input())
for i in range(n):
    c=list(map(str,input().split()))
    if c[0]=="pop":
        s.pop()
    elif c[0]=="remove":
        s.remove(int(c[1]))
    elif c[0]=="discard":
        s.discard(int(c[1]))
print(sum(s))
