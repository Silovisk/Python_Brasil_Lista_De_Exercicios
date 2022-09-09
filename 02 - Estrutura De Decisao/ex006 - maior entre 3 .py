n1 = int(input("Digite o 1° numero :"))
n2 = int(input("Digite o 2° numero :"))
n3 = int(input("Digite o 3° numero :"))

if n1 > n2 and n1 > n3:
  print(f"{n1} maior que {n2} e {n3}")

elif n2 > n1 and n2 > n3:
  print(f"{n2} maior que {n1} e {n3}")

elif n3 > n2 and n3 > n1:
  print(f"{n3} maior que {n1} e {n2}")
elif n1 == n2 or n1 == n3 or n2 == n3:
  print("Numero iguais")
else:
  print("Invalido") 