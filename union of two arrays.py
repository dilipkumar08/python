class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,arr1,arr2):
        count={}
        for  i in arr1+arr2:
            count[i]=0
        
        return len(count)
