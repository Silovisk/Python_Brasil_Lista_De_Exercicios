import random 

def embaralhar_palavra1(palavra: str) -> str:
    letras = list(palavra)  # Converte a palavra em uma lista de letras
    random.shuffle(letras)  # Embaralha a lista de letras
    palavra_embaralhada = ''.join(letras)  # Converte a lista de letras de volta em uma string
    return palavra_embaralhada

def embaralhar_palavra2(palavra):
    # Converte a palavra em uma lista de caracteres
    letras = list(palavra)
    
    # Implementa uma lógica de embaralhamento simples
    for i in range(len(letras)):
        # Escolhe um índice aleatório dentro do intervalo de índices válidos
        indice_aleatorio = random.randint(0, len(letras)-1)
        
        # Troca a letra na posição atual com a letra no índice aleatório
        letras[i], letras[indice_aleatorio] = letras[indice_aleatorio], letras[i]
    
    # Junta os caracteres embaralhados novamente em uma palavra
    palavra_embaralhada = ''.join(letras)
    return palavra_embaralhada

palavra = input("Informe uma palavra: ")


funcoes = [
    embaralhar_palavra1,
    embaralhar_palavra2,
]

for i, funcoes in enumerate(funcoes):
    print(f"Testando {i + 1}°")
    palavra_embaralhada = funcoes(palavra)
    print(palavra_embaralhada)