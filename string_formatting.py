def print_formatted(number):
    w=len(bin(number)[2:])
    for i in range(1,number+1):
        dec=str(i)
        o=oct(i)[2:]
        h=hex(i)[2:].upper()
        b=bin(i)[2:]
        print(dec.rjust(w),o.rjust(w),h.rjust(w),b.rjust(w))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
