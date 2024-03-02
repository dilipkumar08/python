with open('D:\loj.txt','w') as file:#write
    values=[1,2,3,4,5]
    for i in values:
        file.write(str(i)+'\n')
with open('D:\loj.txt','a') as adat:#append
    adata=['d','i','l','i','p']
    for j in adata:
        adat.write(j+'\n')
with open('D:\loj.txt','r') as view:#read
    out=view.read()
    print(out)
