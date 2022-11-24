N,M=map(int,input().split())
X=[]
for _ in range(M):
    X.append(list(map(float,input().split())))
X=zip(*X)
for i in X:
    print("{0:0.1f}".format(sum(i)/len(i)))
