def valorPagamento(valor_prestacao, num_dias_atraso):
    multa_com_atraso = 0.03
    juros_dia = 0.001

    if num_dias_atraso == 0:
        total = valor_prestacao
    elif num_dias_atraso > 0:
        multa = valor_prestacao * multa_com_atraso
        juros = valor_prestacao * juros_dia * num_dias_atraso
        total = valor_prestacao + multa + juros

    return total

cont_prestacao = 0
valor_total_prestacao_com_juros = 0

while True:
    valor_prestacao = float(input("Digite o valor da prestação: "))

    if valor_prestacao == 0:
        break

    num_dias_atraso = int(input("Digite o número de dias em atraso: "))
    valor_prestacao_com_juros = valorPagamento(valor_prestacao, num_dias_atraso)

    print(f"Valor a ser pago: R${valor_prestacao_com_juros:.2f}")

    cont_prestacao += 1
    valor_total_prestacao_com_juros += valor_prestacao_com_juros

print(f"Quantidade de prestações pagas: {cont_prestacao}")
print(f"Valor total de prestações pagas: R${valor_total_prestacao_com_juros:.2f}")
