class Solution:
    def longestPalindrome(self, s: str) -> int:
        store={}
        for i in s:
            try:
                if store[i]:
                    store[i]+=1
            except:
                store[i]=1

        total=sum(store.values())
        res=0
        for j in store.values():
            if j%2==0:
                res+=j
            elif j>2 and (j-1)%2==0:
                res+=j-1
            
        if total>res:
            return res+1
        else:
            return res
------------------------------------------------------------------------------------------
class Solution:
    def longestPalindrome(self, s: str) -> int:
        store={i for i in s}
        val=[s.count(j) for j in store]
        total= sum(val)
        res=0
        for k in val:
            if k%2==0:
                res+=j
            elif k>2 and (k-1)%2==0:
                res+=k-1
            
        if total>res:
            return res+1
        else:
            return res
