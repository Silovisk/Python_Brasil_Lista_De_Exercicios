soma = 0
numero = []
num = 0
print("Digite 0 para encerrar")


while True:
    num = float(input("Digite um número: ")) 
    
    while num > 1000 or num < 0:
        num = float(input("Digite um número[erro]: "))   
    if num != 0:
        soma = soma + num
        numero.append(num)
    else:
        break

print(f"Soma = {soma}")
print(f"Menor numero {min(numero)}")
print(f"Maior numero {max(numero)}")