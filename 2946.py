binaro = int(input(),2)
dabrielgay = int(input())
i = 0
a = []
uepa = False
while i != dabrielgay:
  div = int(input())
  if binaro % div == 0:
    a.append(div)
    uepa = True
  i+=1
if uepa == True:
  j = 0
  a = sorted(a)
  while j != len(a):
    if j != len(a)-1: print("%d " %a[j], end='')
    else: print(a[j])
    j+=1
else: print("Nenhum")
