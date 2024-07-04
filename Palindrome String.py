class Solution:
	def isPalindrome(self, S):
	    res=1
	    temp=-1
		for i in S:
		    if i!=S[temp]:
		        res=0
		        break
		    temp-=1
		return res
