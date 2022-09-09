"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

    Fatorial de: 5
    5! =  5 . 4 . 3 . 2 . 1 = 120
"""
n = int(input("Digite o numero a ser fatorado :"))
cont = n
fat = 1
print(f"!{n} = ",end='')
for i in range(n):
  fat = fat * n 
  n = n - 1 
  print(cont, end=' . ')
  cont -= 1
print("= ",fat)