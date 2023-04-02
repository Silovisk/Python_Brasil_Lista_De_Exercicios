valores = []

for i in range(1, 6):
    valor = float(input(f"Digite o {i}° valor :"))
    valores.append(valor)

valores_inverso = [valores[i] for i in range(len(valores)-1, -1, -1)]

print(f"Os valores digitados foram {valores}")
print(f"Na ordem inversa e {valores_inverso}")