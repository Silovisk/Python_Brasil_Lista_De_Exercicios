dia = int(input("Digite o dia :"))
mes = int(input("Digite o mes :"))
ano = int(input("Digite o ano :"))

if dia <= 31:
  print("dia Valido")
  if mes <= 12:
    print("Mes Valido")
    if ano >= 2021:
      print("Ano Valido")
else:
  print("Invalido")