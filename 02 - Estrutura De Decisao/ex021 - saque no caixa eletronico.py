saque = float(input("Digite o valor do saque maior que 100 :"))

while saque < 100:
  print("Invalido")
  saque = float(input("Digite o valor do saque maior que 100 :"))

n100 = 0
n50 = 0
n10 = 0
n5 = 0
n1 = 0

if saque >= 100:
  n100 = saque // 100
  if saque >= 50:
    n50 = (saque - n100*100) // 50
    if saque >= 10:
      n10 = (saque - n100*100 - n50*50) // 10
      if saque >= 5:
        n5 = (saque - n100*100 - n50*50 - n10*10)// 5
        if saque >= 1:
          n1 = (saque - n100*100 - n50*50 - n10*10 - n5*5)//1
else:
  print("Invalido")

print(f"notas de 100 = {int(n100)} notas\n"
      f"notas de 50  = {int(n50)} notas\n"
      f"notas de 10  = {int(n10)} notas\n"
      f"notas de 5   = {int(n5)} notas\n"
      f"notas de 1   = {int(n1)} notas")
