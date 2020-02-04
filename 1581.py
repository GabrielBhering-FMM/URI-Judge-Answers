num = int(input())
for i in range(1,num+1):
    vet = int(input())
    a = [""]*vet
    cont = 0
    for j in range(0,vet):
        a[j]=input()
    for j in range(0,vet):
        for m in range(0,vet):
            if a[m]==a[j]: cont+=1
    if cont == vet*vet: print(a[0])
    else: print("ingles")
