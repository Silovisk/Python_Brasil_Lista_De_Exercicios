
soma = 0
numero = []
print("Digite 0 para parar ")
while True:
  num = int(input("Informe um valor :"))
  if num != 0:
    soma = soma + num
    numero.append(num)
  else:
    break

print(f"Soma = {soma} ")
print("Menor valor ",min(numero))
print(f"Maior valor ",max(numero))