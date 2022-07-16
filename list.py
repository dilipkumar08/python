if __name__ == '__main__':
    N = int(input())
    a=[]
    b=["insert","print","remove","append","sort","pop","reverse"]
    for n in range(N):
        s=str(input())
        i=s.split(' ')
        if i[0]==b[0]:
            a.insert(int(i[1]),int(i[2]))
        if i[0]==b[1]:    
            print(a)
        if i[0]==b[2]:    
            a.remove(int(i[1]))
        if i[0]==b[3]:
            a.append(int(i[1]))
        if i[0]==b[4]:
            a=sorted(a)
        if i[0]==b[5]:
            a.pop()
        if i[0]==b[6]:
            a=a[::-1]
        
