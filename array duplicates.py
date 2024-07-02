class Solution:
    def duplicates(self, n : int, arr : List[int]) -> List[int]:
        count={}
        
        for i in arr:
            if count.get(i,0)==0:
                count[i]=1
            else:
                count+=1
        res=[]
        for key,value in count.items():
            if value>1:
                res.append(key)
            
        if res:
            return res
        else:
            return [-1]
