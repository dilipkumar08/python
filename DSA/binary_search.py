def binary_search(list,item):
    low=0
    high=len(list)-1
    while low<high:
        mid=(low+high)//2
        if list[mid]==item:
            return mid
        elif list[mid]>item:
            high=mid-1
        else:
            low=mid+1
    return None


print('Index of number 8 in the list is :',binary_search([1,2,3,4,5,6,7,8,9,10],8))
