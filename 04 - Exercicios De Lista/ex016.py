salarios = [0] * 9 # inicializa uma lista com 9 contadores, um para cada intervalo de salário

while True:
    vendas = float(input("Digite o valor das vendas (-1 para encerrar): "))
    if vendas == -1:
        break
    salario = 200 + 0.09 * vendas # calcula o salário do vendedor
    if salario >= 1000:
        salarios[8] += 1
    else:
        salarios[int((salario - 200) // 100)] += 1 # incrementa o contador correspondente ao intervalo de salário

# exibe os resultados
for i in range(len(salarios)):
    if i == 8:
        print("Salários a partir de $1000: ", end="")
    else:
        print(f"Salários de {200+i*100} a {299+i*100}: ", end="")
    print(salarios[i])
