
def prime_factor(n):
    limit=int(n**0.5)+1
    res=0
    while n%2==0:
        res=2
        n//=2
        
    for i in range(3,limit,2):
        while n%i==0:
            res=i
            n//=i
    if n>1:
        return n
    else:
        return res
        
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(prime_factor(n))
