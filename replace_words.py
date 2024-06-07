class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary=set(dictionary)
        length={}
        for i in dictionary:
            length[i]=len(i)
        sentence_split=sentence.split(" ")
        min_size=101
        for temp,words in enumerate(sentence_split):
            for key in length:
                if key==words[:length[key]] and length[key]<min_size:
                    min_size=length[key]
                    sentence_split[temp]=key
            min_size=101
        return (" ".join(sentence_split))
