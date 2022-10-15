def print_rangoli(size):
    a=" abcdefghijklmnopqrstuvwxyz"
    width=(size*4)-3
    for i in range(size,0,-1):
        string=a[size:i:-1]+a[i:size+1]
        string="-".join(string)
        print(string.center(width,'-'))
    for i in range(size-1):
        string=a[size:i+2:-1]+a[i+2:size+1]
        string="-".join(string)
        print(string.center(width,'-'))
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
