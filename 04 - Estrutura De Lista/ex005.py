numeros = []
par = []
impar = []

for i in range(1, 21):
    numero = int(input(f"Digite o {i}° numero: "))
    numeros.append(numero)

impar_ou_par = [par.append(num) if num % 2 == 0 else impar.append(num) for num in numeros]

print(f"""Numeros : {numeros}
Numeros Pares : {par}
Numeros Impares : {impar}
""")