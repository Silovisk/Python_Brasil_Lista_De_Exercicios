vogais = ['a','e','i','o','u']
caracteres = []
consoantes_lidas = []

for i in range(1, 11):
    caractere = str(input(f"Digite o {i}° caractere: ")).lower()
    caracteres.append(caractere)

#caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for caractere in caracteres:
    if caractere not in vogais:
        consoantes_lidas.append(caractere)

print(f"foram lidas {len(consoantes_lidas)} consoantes quais elas sao {consoantes_lidas}")