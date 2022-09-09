n = int(input("Qual numero quer fatorar :"))

fatorial = 1
while n != 1:
  fatorial = fatorial * n 
  n = n - 1
print(f"{fatorial}")