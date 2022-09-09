op = input("Alcool ou Gasolina\nDigite [A] ou [G]\n")

while op.upper() != 'A' and op.upper() != 'G':
  print("Opçao invalida,Tente A ou G\n")
  op = input("Alcool ou Gasolina\nDigite [A] ou [G] :")


if op.upper() == 'A':
  litros = float(input("Digite a quantidade Litros de Alcool :"))
  v_alcool = litros * 1.90
  print(f"Valor sem desconto = R${v_alcool:.2f}")
  if litros <= 20:
    v_alcool = v_alcool - ((litros * 1.90)*0.03)
  elif litros > 20:
    v_alcool = v_alcool - ((litros * 1.90)*0.05)     
  else:
    print("litros Invalido")
  print(f"Valor com desconto = R${v_alcool:.2f}")
elif op.upper() == 'G':
  litros = float(input("Digite a quantidade Litros de Gasolina :"))
  v_gasoli = litros * 2.50
  print(f"Valor sem desconto = R${v_gasoli:.2f}")
  if litros <= 20:
    v_gasoli = v_gasoli - ((litros * 2.50)*0.04) 
  elif litros > 20:
    v_gasoli = v_gasoli - ((litros * 2.50)*0.06)
  else:
    print("Litros Invalido")
  print(f"Valor com desconto = R${v_gasoli:.2f}")
else:
    print("Invalido\n")