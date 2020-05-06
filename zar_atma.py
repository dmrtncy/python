# zar atma uygulaması

import random

while True:
  zar1=random.randint(1,6)
  zar2=random.randint(1,6)
  print("Gelen zarlar: ", zar1," ", zar2)
  a=input("Devam etmek için e ya da E basınız: ")
  if a=="e" or a=="E":
    continue
  else:
    break
