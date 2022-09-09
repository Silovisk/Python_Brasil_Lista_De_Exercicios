numero = int(input("Digite um numero: "))
primo = 0
# exemplo 
# 4   4/1 4/2 4/3 4/4
for i in range(1,numero+1):
    if(numero%i==0):
        primo += 1
if(primo != 2):
    print(f"{numero} Nao e primo")
else:
    print(f"{numero} E primo")