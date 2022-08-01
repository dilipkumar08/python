n=int(input())
for i in range(n):
    try:
        a,b=map(int,input().split())
        print(a//b)
    except Exception as z:
        print("Error Code:",z)
