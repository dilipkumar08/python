from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c=Counter(tasks)
        res=0
        for i in c.values():
            if i==1:
                return -1
                break
            elif i%3==0:
                res+=i//3
            else:
                res+=(i//3)+1
        return res
