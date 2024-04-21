
def factorial(n):  
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
         
n= int(input())
sml=0

while True:
    if sum(factorial(int(digit)) for digit in str(sml))==n:
        print(sml)
        break
    else:
        sml+=1
