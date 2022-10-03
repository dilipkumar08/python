def integer_reversal(N):
    if N>=0:
        reverse_integer=N%10
        N=N//10
        while N>0:
            reverse_integer=(reverse_integer*10)+(N%10)
            N=N//10
        print(reverse_integer)
