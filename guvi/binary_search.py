#binary search
lb=list(map(int,input().split()))
lb.sort()
print(lb)
n=int(input("The value to be found:"))
l=len(lb)
mn=0
mx=l
md=0
while mn<=mx:
    md=(mn+mx)//2
    if lb[md]>n:
        mx=md-1
    elif lb[md]<n:
        mn=md+1
        
if lb[md]==n:
    print("The index of the value in the sorted list is:",md)
else:
    print("The value is not in the list")
