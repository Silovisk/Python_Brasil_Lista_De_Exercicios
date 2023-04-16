def inverter_numero1(numero):
    return str(numero)[::-1]

def inverter_numero2(numero: str) -> str:
    return numero[::-1]

def inverter_numero3(numero: str) -> str:
    return "".join(reversed(numero))

def inverter_numero4(numero: str):
    return [numero[i] for i in range(len(numero) -1, -1, -1)]

numero = int(input("Informe um numero inteiro: "))

funcoes = [
    inverter_numero1,
    inverter_numero2,
    inverter_numero3,
    inverter_numero4,
]

for i, funcoes in enumerate(funcoes):
    print(f"Testando metodo {i + 1}")
    numero_invertido = funcoes(str(numero))

    print(f"Numero : {numero} \nNumero Invertido: {numero_invertido} ", end="\n\n")