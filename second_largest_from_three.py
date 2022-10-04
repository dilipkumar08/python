
def second_largest(A,B,C):
    if A>B and A<C:
        return A
    elif B>A and B<C:
        return B
    elif C>B and C<A:
        return C
    elif C==A or B==A:
        return A
    elif B==C:
        return B
