while True:
    try:
        a,b,c,d,e = input().split("-")
        a = a.lower()
        b = b.lower()
        c = c.lower()
        d = d.lower()
        e = e.lower()
        cont=0
        if(a.find("c")!=-1):
            if(a[0]=="c" or a[len(a)-1]=="c"):
                cont+=1
        if (b.find("o") != -1):
            if(b[0]=="o" or b[len(b)-1]=="o"):
                cont += 1
        if (c.find("b") != -1):
            if(c[0]=="b" or c[len(c)-1]=="b"):
                cont += 1
        if (d.find("o") != -1):
            if(d[0]=="o" or d[len(d)-1]=="o"):
                cont += 1
        if (e.find("l") != -1):
            if(e[0]=="l" or e[len(e)-1]=="l"):
                cont += 1
        if(cont==5): print("GRACE HOPPER")
        else: print("BUG")
    except EOFError:
        break
