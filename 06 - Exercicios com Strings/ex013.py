import random
from unidecode import unidecode

def embaralhar_palavra(palavra: str) -> str:
    # Converte a string em uma lista de caracteres
    lista_caracteres = list(palavra)

    # Embaralha a lista de caracteres
    random.shuffle(lista_caracteres)

    # Converte a lista de caracteres de volta para uma string
    palavra_embaralhada = ''.join(lista_caracteres)

    return palavra_embaralhada

def limpar_palavra(palavra):
    # Usa a função unidecode() para remover acentuações
    palavra = unidecode(palavra)
    # Usa o método replace() para remover o caracter '-'
    palavra = palavra.replace('-', '')
    return palavra

palavras = ['abacaxi', 'alicate', 'amarelo', 'arco-íris', 'astronauta', 'avião', 'bala', 'bicicleta', 'borboleta', 'cachorro',
            'cadeira', 'camarão', 'caneta', 'carro', 'casa', 'chave', 'chocolate', 'computador', 'dinossauro', 'elefante',
            'escova', 'espelho', 'faca', 'fogão', 'guitarra', 'helicoptero', 'hipopótamo', 'igreja', 'janela', 'leão', 'livro',
            'macaco', 'martelo', 'melancia', 'microfone', 'mochila', 'navio', 'ninho', 'óculos', 'papagaio', 'pato', 'pincel',
            'pipoca', 'porta', 'queijo', 'relógio', 'sapato', 'tartaruga', 'telefone', 'uva', 'violinista']



palavra = random.choice(palavras)
palavra = limpar_palavra(palavra)

palavra_embaralhada = embaralhar_palavra(palavra)
vidas = 6


print(f"A palavra embaralhada e : {palavra_embaralhada}\n\tTente adivinhar")

while True:
    palavra_jogador = str(input("Adivinhe a palavra: "))

    if palavra_jogador == palavra:
        print("Parabens voce acertou!")
        break
    else:
        print("Voce errou!")
        vidas -= 1
        print(f"Voce ainda tem {vidas} vidas")
    
    print()
    if vidas == 5:
        print(f"1° Dica: A primeira letra e: {palavra[0]}")
    elif vidas == 3:
        print(f"2° Dica: A ultima letra e: {palavra[len(palavra)-1]}")
    elif vidas == 1:
        print(f"3° Dica: A segunda letra e: {palavra[1]}")
    
    if vidas == 0:
        print(f"Voce perdeu! a palavra correta era {palavra}")
        break
