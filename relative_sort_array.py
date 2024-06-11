class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort()
        count=Counter(arr1)
        res=[]
        for i in arr2:
            
            for j in range(count[i]):
                res.append(i)
            del count[i]
        print(count)
        for k in count:
            for l in range(count[k]):
                res.append(k)
        return res
        
