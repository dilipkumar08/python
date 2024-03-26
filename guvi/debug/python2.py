n = int(input())
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
list1.extend(list2)
list1.sort()
while(n>0):
 if(n > 0):
     print(list1[n-1] + list1[n])
     break

