class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd,res=0,0
        left,middle=0,0

        for r in range(len(nums)):
            if nums[r]%2!=0:
                odd+=1
            while odd>k:
                if nums[left]%2:
                    odd-=1
                left+=1
                middle=left
            if odd==k:
                while not nums[middle]%2:
                    middle+=1
                res+=(middle-left)+1
        return res



