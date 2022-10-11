def string_series(string):
    l=len(string)+1
    print("\n"+string,"->",end=" ")
    for i in range(1,l):
        print(string[:i],end=" ")
if "__main__"==__name__:
    string=str(input("Enter a String: "))
    string_series(string)
