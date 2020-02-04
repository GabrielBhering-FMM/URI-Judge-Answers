e,d = input().split()
e,d = [int(e), int(d)]
res = d-e
if(e>d): print("Eu odeio a professora!")
elif(res<3):
    print("Parece o trabalho do meu filho!")
    d = d + 2
    if(d<=24): print("TCC Apresentado!")
    if(d>24): print("Fail! Entao eh nataaaaal!")
else: print("Muito bem! Apresenta antes do Natal!")
