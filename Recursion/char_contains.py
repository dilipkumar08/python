def contains(s:str,ch:chr):
    res=False
    if s!='' and ch!='':
        if s[0]!=ch:
            s=s[1:]
            res=contains(s,ch)
        else:
            s=''
            return True
    return res
