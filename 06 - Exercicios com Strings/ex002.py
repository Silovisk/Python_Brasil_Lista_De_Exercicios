def inverte_nome1(nome):
    cont = len(nome) - 1
    nome_invertido = ""

    while cont >= 0:    
        nome_invertido += nome[cont]
        cont -= 1

    return nome_invertido

def inverte_nome2(nome):
    return "".join([nome[i] for i in range(len(nome) -1, -1, -1)])
        #nome_contrario = "".join(nome_contrario)

def inverte_nome3(nome):
    return nome[::-1]

nome = input("Informe seu nome: ").upper()

funcoes = [
    inverte_nome1,
    inverte_nome2,
    inverte_nome3
]

print(f"Seu Nome: {nome}")

for i, funcoes in enumerate(funcoes):
    nome_contrario = funcoes(nome.upper())
    print(f"Seu nome ao contrario {i+1}° metodo {nome_contrario}")