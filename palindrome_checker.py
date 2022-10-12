def palindrome_checker(word):
    l=len(word)-1
    m=(l+1)//2
    temp=0
    for i in range(m):
        if word[i]==word[l]:
            temp+=1
        else:
            temp-=1
        l-=1
    if temp==m:
        print(word,'->','true')
    else:
        print(word,'->','false')
        
if __name__=="__main__":
    word=str(input("Enter a word: "))
    palindrome_checker(word)
