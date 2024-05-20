def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    l=len(arrivals)
    ind=arrivals.index(name)
    if arrivals[-1]==name:
        return False
    if l%2==0:
        if l//2- 1<ind:
            return True
        else:
            return False
    else:
        if l//2 +1<=ind:
            return True
            
        else:
            return False
  

