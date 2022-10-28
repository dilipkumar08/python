def containsNegativePair(ArrayList: list[int],index=0):
    try:
        if -(ArrayList[index])==ArrayList[index+1]:
            return True
        else:
            return containsNegativePair(ArrayList,index=index+1)
    except:
        if type(ArrayList)!=list:
            return "Invalid Input Type"
        return False
