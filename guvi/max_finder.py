#finding max

def max_finder(val: list):
    a=val[0]
    for i in val[1:]:
        if a<i:
            a=i
    return a
        
li =list(map(int,input().split()))
print("The max of the given list :",max_finder(li))
