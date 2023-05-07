def numero_por_extenso(numero):
    unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
    dezenas_1 = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
    dezenas_2 = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
    numero_extenso = ""
    verifica = False

    if numero > 99 or numero < 0:
        return False

    dezena = numero // 10
    unidade = numero % 10

    if dezena == 0:
        numero_extenso = unidades[unidade]
    elif dezena == 1:
        numero_extenso = dezenas_1[unidade]
    else:
        if unidade == 0:
            numero_extenso = dezenas_2[dezena-2]
        else:
            numero_extenso = f"{dezenas_2[dezena-2]} e {unidades[unidade]}"

    return numero_extenso


#numero = int(input('Digite um número de 0 até 99: '))


for i in range(0, 101):
    print(f"{i} - {numero_por_extenso(i)}")
