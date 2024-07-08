class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        test=head
        length=1
        res=head
        
        while test and test.next:
            test=test.next
            length+=1
            
            
        for i in range(length//2):
            res=res.next
        
        return res.data
