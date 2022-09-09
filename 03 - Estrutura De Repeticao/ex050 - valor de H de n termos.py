h = 1;soma=1
n_termos = int(input("Digite o valor de N termos:"))+1


for i in range(2,n_termos):
    print(f"{h}/{i}")
    soma += h/i

print(f"O valor de H e igual a {soma:.4f}")