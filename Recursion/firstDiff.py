def firstDiff(s:str,t:str,index=0):
    res=0
    if s==''and t!=''or s!='' and t=='':
        return res
    elif t!=''and s!='':
        try:
            if s[index]==t[index]:
                res=firstDiff(s,t,index=index+1)            
            else:
                return index
        except:
            return index
    return res
