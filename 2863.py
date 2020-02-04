while True:
    try:
        i = 0
        t = int(input())
        a = [None]*t
        while i != t:
            a[i] = float(input())
            i+=1
        x = min(a)
        print(x)
    except EOFError:
        break
