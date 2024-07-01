
class Solution:
    def maxSubArraySum(self,arr):
        current,total=arr[0],arr[0]
        for i in range(1,len(arr)):
            current=max(arr[i],current+arr[i])
            if current>total:
                total=current
        
        return total
