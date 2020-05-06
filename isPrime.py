a=int(input("Son sayı?: "))

for i in range(2,a):
  isPrm=True
  for j in range(2,(i//2)+1):
    if i%j==0:
      isPrm=False
      break
  if isPrm==True:
    print(i)
  
