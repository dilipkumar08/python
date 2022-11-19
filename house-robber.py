#Method-1
class Solution:
    def rob(self, nums: List[int]) -> int:
        r1=0
        r2=0
        for i in nums:
            temp=max(i+r1,r2)
            r1=r2
            r2=temp
        return r2
      
#method-2     
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        l=len(nums)
        if l<3: return max(nums)
        
        dp=[0]*l
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,l):
            dp[i]=max(nums[i]+dp[i-2],dp[i-1])
        return dp[-1]
