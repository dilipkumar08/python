alpha={'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
words={}
li=[]
for i in range(int(input())):
    li.append(input())

temp=1
li.sort()
for j in li:
    value=0
    for k in j:
       value+= alpha[k]
    words[j]=[temp,value]
    temp+=1
    
q=int(input())
for k in range(q):
    query=input()
    print(words[query][0]*words[query][1])
    
