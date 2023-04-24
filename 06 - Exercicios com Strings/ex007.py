vogais = ['a', 'e', 'i', 'o', 'u']

string = str(input("Informe uma string: "))

cont_espacos = cont_vogais = 0

for s in string:
    if s == " ":
        cont_espacos += 1 
    
    if s in vogais:
        cont_vogais += 1


print(f"""
A String: {string}
Quantidade de espacos em brancos: {cont_espacos}
Quantidade de vogais: {cont_vogais}
""")