def anagram(string1,string2):
    #sorting strings 
    s1=sorted(string1.lower())
    s2=sorted(string2.lower())
    if s1==s2:
        print("The given inputs are  a anagram")
    else:
        print("The given inputs are not a anagram")
    return 0

input1=input("Enter the string 1:")
input2=input("Enter the string 2:")
anagram(input1,input2)
    
