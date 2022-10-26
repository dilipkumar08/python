
def oneAway(s:str,t:str,temp=-1):
    res=False
    if temp==-1:
        if len(s)!=len(t):
            return False
        elif len(s)==0 or len(t)==0 :
            return "Invaid"
        else:
            temp=temp+1
    if temp<2 and s!='' and t!='':

            if s[0]==t[0]:
                s=s[1:]
                t=t[1:]
                res=oneAway(s,t,temp)
            else:
                s=s[1:]
                t=t[1:]
                res=oneAway(s,t,temp=temp+1)
    else:
        if  temp==1:
            return True
    return res
