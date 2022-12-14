def binary_search(lst, target):
    start = 0
    end = len(lst) - 1
    while(start <= end):
        mid_val = (start + end) // 2
        if(lst[mid_val] > target):
            end = mid_val - 1
        elif(lst[mid_val] < target):
            start = mid_val + 1
        else:
            return mid_val
    return None
