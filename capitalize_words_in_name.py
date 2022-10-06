if __name__=="__main__":
    name=list(map(str,input("Please Enter your name in lowercase:").strip().split()))
    l=len(name)
    for i in range(l):
        name[i]=name[i].capitalize()
    print(" ".join(name))
