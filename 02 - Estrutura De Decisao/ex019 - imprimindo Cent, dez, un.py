num = int(input("Digite um numero :"))
 
while num > 1000:
  print(f"{num} nao pode ser > que 1000")
  num = int(input("Digite um numero :"))
  
cen = num//100
dez = num//10 - cen*10 
un = num - cen*100 - dez*10

print(
  f"Centenas = {cen}\n"
  f"Dezenas = {dez}\n"
  f"Unidade = {un}\n")
      
      