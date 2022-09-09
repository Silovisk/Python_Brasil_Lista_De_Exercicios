i = 0
soma=0

number = int(input(f"Digite o {i}° numero :"))

for i in range(4):
  number = int(input(f"Digite o {i+1}° numero :"))
  soma += number

print(soma)
media = soma/5
print(media)