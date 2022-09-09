print("-Bem vindo ao Hipermercado Tabajara-\n====================================")
nome = input("Digite seu nome:")
op = int(input("Digite uma das opçoes\n"
      "--------------------------------------------------------\n"
	    "| 	   TIPO	      |   Até 5 Kg       |	 Acima de 5 Kg |\n"
      "|[1] - File Duplo | R$ 4,90 por Kg   | R$ 5,80 por Kg  |\n"
      "|[2] - Alcatra    | R$ 5,90 por Kg   | R$ 6,80 por Kg  |\n"
      "|[3] - Picanha    | R$ 6,90 por Kg   | R$ 7,80 por Kg  |\n"
      "--------------------------------------------------------\n\n---"))

kg = float(input("Quantidade em Kg:"))

op_pag = int(input("\nDigite uma das opçoes\n"
      "------------------------------------------\n"
	    "| 	   TIPO	              |   DESCONTO(%)|\n"
      "|[1] - Dinheiro           |      0%      |\n"
      "|[2] - Cartão Tabajara    |      5%      |\n"
      "|[3] - Cartão Comum       |      0%      |\n"
      "------------------------------------------\n\n---"))


if op == 1:
  tipo = 'File Duplo'
  if kg <= 5:
    valor = 4.90*kg
  elif kg > 5:
    valor = 5.80*kg
elif op == 2:
  tipo = 'Alcatra'
  if kg <= 5:
    valor = 5.90*kg
  elif kg > 5:
    valor = 6.80*kg
elif op == 3:
  tipo = 'Picanha'
  if kg <= 5:
    valor = 6.90*kg
  elif kg > 5:
    valor = 7.80*kg
else:
  print("Opçao invalida")
  
if op_pag == 1:
  tipo_pag = 'Dinheiro'
  desconto = 0
elif op_pag == 2:
  tipo_pag = 'Cartão Tabajara'
  desconto = valor * 0.05
elif op_pag == 3:
  tipo_pag = 'Cartão Comum'
  desconto = 0
else:
  print("Opçao invalida")


print("=================CUPOM FISCAL==================")
print("===============================================")
print(f"| Nome: {nome.upper()}                       ")
print(f"| Tipo da carne: {tipo.upper()}              ")
print(f"| Quantidade da carne: {kg:.2f} Kg           ")
print(f"| Preço total: R${valor:.2f}                 ")
print(f"| Tipo de pagamento: {tipo_pag.upper()}      ")
print(f"| valor do desconto: R${desconto:.2f}        ")
print(f"| Total a pagar:  {valor-desconto:.2f}       ")
print("===============================================")

