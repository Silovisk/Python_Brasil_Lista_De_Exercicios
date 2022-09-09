n = int(input("Digite um numero: "))
primo = 0

for i in range(1, n+1):
    primo += 1 if n % i == 0 else 0
    txt = "primo" if primo == 2 else "Nao primo"
print(f"{n} - {txt}")
