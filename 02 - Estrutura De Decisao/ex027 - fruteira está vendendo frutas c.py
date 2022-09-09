kg_morango = float(input("Digite a quantide de kg de morango :")) 
kg_maca = float(input("Digite a quantidade de kg de maça :"))

if kg_morango <= 5:
  valor_morango = 2.50 * kg_morango
elif kg_morango > 5:
  valor_morango = 2.20 * kg_morango
else:
  print("kg morango Invalido")

if kg_maca <=5:
  valor_maca = 1.80 * kg_maca
elif kg_maca > 5:
  valor_maca = 1.50 * kg_maca
else:
  print("kg maca Invalido")

total = valor_maca+valor_morango
total_kg = kg_maca+kg_morango

if total_kg > 8 or total > 25:
  total = total+total*0.1

print(f"Total de Kg comprado {total_kg}Kg")
print(f"Total a ser pago e de R${total:.2f}")