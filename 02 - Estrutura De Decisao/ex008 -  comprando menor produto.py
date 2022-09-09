p1 = float(input("Digite o preço do 1° produto :"))
p2 = float(input("Digite o preço do 2° produto :"))
p3 = float(input("Digite o preço do 3° produto :"))

if p1 < p2 and p1 < p3:
  comprar = p1 
elif p2 < p1 and p2 < p3:
  comprar = p2
else:
  comprar = p3

print("Voce devera comprar o produto  :{}".format(comprar))