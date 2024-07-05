def smallest(arr):
    index,small=0,arr[0]
    l=len(arr)
    for i in range(1,l):
        if arr[i]<small:
            small=arr[i]
            index=i
    return (small,index)

def selection_sort(arr):
    sorted_arr=[]
    while arr:
        small,index=smallest(arr)
        arr.pop(index)
        sorted_arr.append(small)
    return sorted_arr

if __name__=='__main__':
    arr=[2,1,7,5,3,2,9,7,8]
    print('sorted array:',selection_sort(arr))
