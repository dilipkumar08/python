class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        sample=Counter(words[0])

        for i in words[1:]:

            temp=Counter(i)

            for j in sample:

                sample[j]=min(sample[j],temp[j])
        res=[]

        for k in sample:

            for l in range(sample[k]):

                res.append(k)
        
        return res
            
