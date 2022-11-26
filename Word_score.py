n=int(input())
vowels=["a","e","i","o","u","y"]
words=list(map(str,input().split()))
score=0
for i in words:
    temp=0
    for j in i:
        if j in vowels:
            temp+=1
    if temp%2==0:
        score+=2
    else:
        score+=1
print(score)
