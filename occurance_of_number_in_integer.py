N=int(input("Enter the integer:"))
n=int(input("Enter the number(0-9): ")
count=0
while N>n-1:
  if N%10==n:
    count+=1
    N=N//10
    print(count)
