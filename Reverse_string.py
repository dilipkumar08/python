class Solution:
    def reverseString(self, s: List[str]) -> None:
        l=len(s)-1
        for i in range(0,(l+1)//2):
            s[i],s[l-i]=s[l-i],s[i]
        
