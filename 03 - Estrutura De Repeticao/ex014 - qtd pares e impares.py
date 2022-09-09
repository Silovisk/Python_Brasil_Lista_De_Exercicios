soma = 0
i = 0
par = 0
impar = 0
for i in range(10):

    num = int(input("Digite um numero : "))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"Numeros impares : {impar}")
print(f"Numeros pares : {par}")


