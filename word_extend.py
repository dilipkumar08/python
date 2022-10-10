def word_extend(word):
    l=len(word)-1
    if l==0:
        return word
    else:
        m=(l+2)//2
        n=m
        temp1=''
        temp2=''
        for i in range(m):
            temp1+=word[i]*n
            temp2+=word[l]*n
            l-=1
            n-=1
        return(temp1[:-1]+temp2[::-1])

if __name__=="__main__":
    word=str(input("Enter a word with an odd number of letters: "))
    print(word,"->",word_extend(word))
