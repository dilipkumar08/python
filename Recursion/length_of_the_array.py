def num_count(arr):
    if arr==[]:
        return 0
    else:
        arr.pop()
        return 1+num_count(arr)
num_count([1,2,3,4,5,6])
