#To check whether x can be divided by 2,3 and 5
x=int(input("Enter the value for x:"))

if x%2==0:
    if x%3==0:
        if x%5==0:
            print("x can be divided by 2, 3 & 5 ")
        else:
            print("x can only be divided by 2 and 3 but not 5")
    else:
        print("x can only be divided by 2")
elif x%3==0:
    if x%5==0:
        print("x can only be divided by 3 and 5 but not 2")
    else:
        print("x can only be divided by 3")
elif x%5==0:
    print("x can only be divided by 5")
else:
    print("x cannot be divided with 2,3 and 5")
        
    
