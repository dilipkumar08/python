n=int(input())
for i in range(n):
    power=2**int(input())
    res=0
    while power:
        res+=power%10
        power=power//10
    print(res)
    

    
