n_termos = int(input("Digite o numero de termos :"))
j = 1
for i in range(1,n_termos,2):
    print(f"{j}/{i}")
    j += 1
    soma = j/i

print(f"A Soma dos termos e {soma:.4f}")