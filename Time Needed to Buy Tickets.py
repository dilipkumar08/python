class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        l=len(tickets)
        res=tickets[k]
        for i in range(l):
            if i<k:
                if tickets[i]<=tickets[k]:
                    res+=tickets[i]
                elif tickets[i]>tickets[k]:
                    res+=tickets[k]
   
            if i>k:
                if tickets[i]<tickets[k]:
                    res+=tickets[i]
                elif tickets[i]>=tickets[k]:
                    res+=tickets[k]-1

        return res 
