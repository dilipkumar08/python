def bitflip(s:str,temp=''):
    try:
        if s[0]=='1':
            temp+='0'
            s=s[1:]
        elif s[0]=='0':
            temp+='1'
            s=s[1:]
        else:
            temp+=s[0]
            s=s[1:]
        s=bitflip(s,temp)
    except:
        if temp=="":
            return "Invalid"
        return temp
    
    return s
