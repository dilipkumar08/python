tf=np.array([[1,2,3],[2,3,4],[6,7,8],[2,3,4]])
m=len(tf)
n=len(tf[0])
m=-(m-2)
n=n-1
print(tf)
for i in range(m,n):
    print(tf.diagonal(i))


#incase if you want to print the single size diagonals change m=-(m-1) and n=n
