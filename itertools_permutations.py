from itertools import permutations
result=[]
string, length = input().split()
for i in permutations(string,int(length)):
    result.append("".join(i))
result=sorted(result)
print('\n'.join(result))
