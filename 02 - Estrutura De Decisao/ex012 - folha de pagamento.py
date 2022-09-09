valor_hora = float(input("Digite o valor da sua hora :"))
horas_trab = int(input("Digite a quantidade de horas trabalhadas:"))

salario_bruto = valor_hora * horas_trab

if salario_bruto <= 900:
  desc_ir = 'isento'
elif salario_bruto <= 1500:
  desc_ir = 5/100
elif salario_bruto <= 2500:
  desc_ir = 10/100
elif salario_bruto > 2500:
  desc_ir = 20/100

IR = salario_bruto * desc_ir
INSS = salario_bruto * (10/100)
FGTS = salario_bruto * (11/100)

descontos = IR + INSS  
salario_liquido = salario_bruto - descontos


print(f"     Salário Bruto: ({valor_hora} * {horas_trab})    : R$ {salario_bruto}")
print(f"     (-) IR ({desc_ir*100}%)                 : R$ {IR}")  
print(f"     (-) INSS (10%)                : R$ {INSS}")
print(f"     (+) FGTS (11%)                : R$ {FGTS}")
print(f"     Total de descontos            : R$ {descontos}")
print(f"     Salário Liquido               : R$ {salario_liquido}")