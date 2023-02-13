def bubble_sort(a):
    print("Working mechanism")
    for i in range(0,len(a)):
        for j in range(i+1,len(a)-1):
            print(a[i],a[j])
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
            print(a[i],a[j])
        print("-----------------------------")
    return a
