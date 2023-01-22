def collatz(number):
    if number==0:
        return "Pass a number greater than 0"
    elif number==1:
        return number
    elif number%2==0:
        print(number)
        return collatz(number//2)
    elif number%2==1:
        print(number)
        return collatz((3*number)+1)
