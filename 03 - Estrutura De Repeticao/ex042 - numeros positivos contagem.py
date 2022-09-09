n = int(input("Digite um numero para começar:"))

s1 = s2 = s3 = s4 = 0

while n > -1:
    n = int(input("Digite um numero de 0 ate 100 :"))

    if (n >= 0 and n <= 25):
        s1 += 1
    elif(n >= 26 and n <= 50):
        s2 += 1
    elif(n >= 51 and n <= 75):
        s3 += 1
    elif(n >= 76 and n <= 100):
        s4 += 1

print(f"Lista de numeros entre \n[0 - 25] = {s1}\n[26 - 50] = {s2}\n[51 - 75] = {s3}\n[76 - 100] = {s4}")