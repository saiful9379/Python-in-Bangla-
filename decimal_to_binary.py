while True:
    n  = int(input())
    l = []
    while n != 0:
        fact = n//2
        rem = n -2* fact
        n = fact
        l.append(rem)
    x = "".join(str(i) for i in l[::-1])
    print(n,"Binary is :",x)
