val_hora = float(input("Quanto ganha por hora :"))
horas_trab = int(input("Digite quanto trabalha por hora :"))

salario_bruto = val_hora * horas_trab
IR = salario_bruto * (11/100)
INSS = salario_bruto * (8/100)
sindicato = salario_bruto * (5/100)
salario_liquido = salario_bruto - IR - INSS - sindicato

print(f"- Salário Bruto : R$ {salario_bruto}\n"
      f"- IR (11%) : R$ {IR} \n"
      f"- INSS (8%) : R$ {INSS}\n"
      f"- Sindicato (5%) : R$ {sindicato}\n"
      f"= Salário Liquido : R$ {salario_liquido}\n")