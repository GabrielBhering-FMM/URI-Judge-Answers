while(True):
    cont=0
    bruh=0
    b = input()
    a = b.lower()
    if(a=="*"): break
    for i in range(len(a)):
        if(a[i]==" "):
            bruh+=1
            if(a[0]==a[i+1]): cont +=1
    if(cont==bruh): print("Y")
    else: print("N")
