l=0
while True:
    try:
        
        pens=False
        a = int(input())
        if(l>0): print("")
        l+=1
        if((a%4==0 and a%100!=0 )or a%400==0):
            print("This is leap year.")
            pens = True
        if(a%15==0): print("This is huluculu festival year.")
        elif(not pens): print("This is an ordinary year.")
        if(pens and a%55==0): print("This is bulukulu festival year.")
    except EOFError: break
