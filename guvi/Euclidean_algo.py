#Euclidean algorithm

a=int(input("val 1: "))
b=int(input("val 2: "))

while b:
    a,b=b,a%b
print(a)
