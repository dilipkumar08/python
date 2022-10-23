def isBinary(s:str,index=None):
    res=True
    if s!="":
        try:
            index=0
            if s[0]=='1' or s[0]=='0':
                s=s[1:]
                res=isBinary(s,index)
            else:
                return False
        except:
            return False
    else:
        if index==None:
            return "invalid"
    return res
