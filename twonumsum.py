def twoNumberSum(array, targetSum):
    o=0
    w=[]
    b=len(array)
    for i in array:
        o=o+1
        for j in array[o:b]:
            sum=i+j
            if sum==targetSum:
                w=[i,j]
                break;
    return(w)
    
if __name__ == "__main__":
  array=[3,5,-4,8,11,1,-1,6]
  target=10
  print(twoNumberSum(array,target))
