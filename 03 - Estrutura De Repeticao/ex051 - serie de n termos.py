m = int(input("Informe quantos termos voce deseja :"))
n = 1
soma = 0
for i in range(1,m,2):
    print(f"{n}/{i}")
    soma += n/i 
    n += 1

print(f"A soma e :{soma:.4f}")