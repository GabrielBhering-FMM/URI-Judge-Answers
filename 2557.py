while True:
    try:

        a = input()
        for i in (range(len(a))):
            if(a[i]=="+"):
                membro1 = a[:i]
                a = a[i+1:]
                break
        for i in (range(len(a))):
            if(a[i]=="="):
                membro2 = a[:i]
                a = a[i+1:]
                break

        if(membro1=="R" or membro1=="L" or membro1=="J"):
            print(int(a)-int(membro2))
        elif(membro2=="R" or membro2=="L" or membro2=="J"):
            print(int(a)-int(membro1))
        else:
            print(int(membro1)+int(membro2))
    
    except EOFError:
        break
