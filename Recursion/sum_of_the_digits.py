def digisum(n):
    if n==0:
        return 0
    else:
        return n%10+digisum(n//10)
