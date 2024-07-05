def quick_sort(arr):
    if len(arr)<2:
        return arr
    elif len(arr)==2:
        if arr[0]>arr[1]:
            arr[0],arr[1]=arr[1],arr[0]
        return arr
    else:
        temp=arr[0]
        lower=[i for i in arr[1:] if i<temp]
        higher=[j for j in arr[1:] if j
                1>=temp]

        return quick_sort(lower)+[temp]+quick_sort(higher)

if __name__=="__main__":
    arr=[3,45,6,7,9,12,10,2,56]
    print("Sorted array :",quick_sort(arr))
