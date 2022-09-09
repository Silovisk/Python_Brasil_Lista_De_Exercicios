numero = int(input("Digite um numero: "))
primo = 0
# exemplo 
# 4   4/1 4/2 4/3 4/4
for i in range(1,numero+1):
    if(numero%i==0):
        primo += 1
        print(f"{numero} e divisivel por {numero}/{i} = 0")
    
txt = "Nao e primo" if primo != 2 else "E primo"

print(f"{numero} {txt}")

"""
if(primo != 2):
    print(f"{numero} Nao e primo")
else:
    print(f"{numero} E primo")
"""