n,m=map(int,input().split())
symbol=".|."
#for the first part of design
for i in range(n):
    if not i%2==0:
        print((symbol*i).center(m,"-"))
        
# for center part of design       
print("WELCOME".center(m,"-"))

#for last part of the design
for j in reversed(range(n)):
        if not j%2==0:
            print((symbol*j).center(m,"-"))
