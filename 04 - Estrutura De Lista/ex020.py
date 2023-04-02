salarios = []
salario = -1

abono = cont_valor_minimo_pago = 0
abonos = []


while True:
    if salario == 0:
        break
    salario = float(input("Informe seu salario (0 = Fim): "))
    salarios.append(salario)       

salarios.remove(0)

print("Salario   -   Abono")
for i in range(len(salarios)):

    abonos.append(salarios[i] * (20 / 100)) # Calculo 20% do salario bruto de dezembro
    if abonos[i] <= 100.0:
        abonos[i] = 100.0
        cont_valor_minimo_pago += 1

    print(f"R$ {salarios[i]} -- R$ {abonos[i]}", end="\n")


print(f"""
Foram processados {len(salarios)} colaboradores
Total gasto com abono R$ {sum(abonos)}
Valor minimo pago a {cont_valor_minimo_pago} colaboradores
Maior valor de abono pago: R$ {max(abonos)}

""")
