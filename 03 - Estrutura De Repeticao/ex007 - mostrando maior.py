i = 1

n = int(input(f'Digite o {i}° numero : '))
maior = n

while i < 5:
  n = int(input(f'Digite o {i+1}° numero : '))

  if n > maior:
    maior = n
  i += 1
print(maior)
