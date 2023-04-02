valores = []

for i in range(1, 6):
    valor = int(input(f"Digite o {i}° valor: "))
    valores.append(valor)

mult = valores[0] 
for i in range(len(valores)):
    print(mult)
    mult = mult * valores[i]

print(f"""
Numeros : {valores}
Soma : {sum(valores)}
multiplicacao : {mult}

""")