def contar_digitos_numero_inteiro1(numero):
    cont = 0
    for n in str(numero):
        cont += 1   
    return cont

def contar_digitos_numero_inteiro2(numero):
    return sum(1 for n in str(numero))

def contar_digitos_numero_inteiro3(numero):
    return str(len(str(numero)))

numero = int(input("Informe um numero inteiro: "))

funcoes = [
    contar_digitos_numero_inteiro1, 
    contar_digitos_numero_inteiro2, 
    contar_digitos_numero_inteiro3, 
]

for i, funcao in enumerate(funcoes):
    print(f"Testando método {i + 1}")
    quantidade_digitos = funcao(numero)
    print(f"A quantidade de digitos que o número {numero} possui é {quantidade_digitos}")