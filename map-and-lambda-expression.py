cube = lambda x: x**3 

def fibonacci(n):
    li=[]
    i=0;j=1
    for _ in range(n):
        li.append(i)
        i=j
        j+=li[_]
    return li
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
