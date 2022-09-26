for _ in range(int(input())):
    len_a, a = int(input()), set(map(int,input().split()))
    len_b, b = int(input()), set(map(int, input().split()))
    print(a.issubset(b))
