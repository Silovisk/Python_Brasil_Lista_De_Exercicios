salario = float(input("Digite o Salario do colaborador: "))

if salario <= 280:
  p = 20/100
elif salario > 280 and salario <= 700:
  p = 15/100
elif salario > 700 and salario <= 1500:
  p = 10/100
elif salario > 1500:
  p = 5/100
else:
  print("Invalido!")  

aumento =  salario * p
salario_novo = salario + aumento

print("o salário antes do reajuste :",salario)
print(f"o percentual de aumento aplicado : {p*100}%")
print("o valor do aumento :",aumento)
print("o novo salário, após o aumento :",salario_novo)