n = float(input("Informe o numero :"))
op = int(input("Qual operaçao deseja executar ?\n"
            "[1] - Par ou impar:\n"
            "[2] - Positivo ou negativo:\n"
            "[3] - inteiro ou decimal:\n"))

while op != 1 and op != 2 and op != 3:
    print("Opçao incorreta tente 1 ou 2 ou 3")
    op = int(input("Qual operaçao deseja executar ?\n"
            "[1] - Par ou impar:\n"
            "[2] - Positivo ou negativo:\n"
            "[3] - inteiro ou decimal:\n"))


if op == 1:
  if n%2==0:
      print(f"{n} e par")
  else:
      print(f"{n} e impar")  
elif op == 2:
  if n>0:
      print(f"{n} e positivo")
  elif n<0:
    print(f"{n} e negativo")
  else:
    print(f"{n} e igual a 0")
elif op == 3:
  if n == round(n):
    print(f"{n} e inteiro")
  else:
    print(f"{n} e decimal")
else:
    print("Invalido")          