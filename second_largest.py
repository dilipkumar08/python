a=[2,200,2000,3034,5,1000,76,3,2,1,154,7,4,33]
first=0
second=0
for  i in a[1:]:
    if i>first:
        second=first
        first=i
    elif i>second and second<first and i<first:
        second=i
print(f"The second largest is: {second} ")
        
        
