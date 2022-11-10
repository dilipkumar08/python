n = int(input())
s = set(map(int,input().split()))

for i in range(int(input())):
    n = input().split()
    s1 = set(map(int, input().split()))
    if "intersection_update" in n:
        s.intersection_update(s1)
    elif "update" in n:
        s.update(s1)
    elif "symmetric_difference_update" in n:
        s.symmetric_difference_update(s1)
    else:
        s.difference_update(s1)

print(sum(s))
