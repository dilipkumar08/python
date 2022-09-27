from collections import OrderedDict
n, dct = int(input()), OrderedDict()

for _ in range(n):
    
    *name, price = tuple(map(str, input().split()))   
    name, price = " ".join(name), int(price)
    
    if name in dct:
        dct[name] += price
    else:
        dct[name] = price

for k, v in dct.items():
    print(k, v)
