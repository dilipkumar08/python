N=int(input("Enter the integer:"))
first_digit=0
last_digit=0
if N>9:
    last_digit=N%10
    while N!=0:
        if N<10:
            first_digit=N
        N=N//10
    print(first_digit+last_digit)
