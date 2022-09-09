n = float(input("Digite um numero :"))

if n == round(n):
  print(f'O numero {n} e inteiro')
else:
  print(f'O numero {n} e decimal')
  print(f'Arredondado n positivo :{round(n)}')