def valid_triangle(A,B,C):
    if A>0 and B>0 and C>0 and A+B+C==180.00:
        print("Valid Triangle")
    else:
        print("Invalid Triangle")
if __name__=="__main__":
    A=float(input("Angle A:"))
    B=float(input("Angle B:"))
    C=float(input("Angle C:"))
    valid_triangle(A,B,C
