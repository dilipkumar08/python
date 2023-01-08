def wrapper(f):
    def fun(l):
        lst = []
        for n in l:
            x = str(n[-10:])
            ph = '+91 '+x[:5]+' '+x[5:]
            lst.append(ph)
        lst.sort()
        for i in lst:
            print(i)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
