class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res=0
        l=len(nums)
        for i in range(l):
            for j in range(i+1,l+1):                
                if sum(nums[i:j])%k==0:
                    res+=1
        return res
        
