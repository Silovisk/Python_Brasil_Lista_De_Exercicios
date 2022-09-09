area_pintar = float(input("Digite a area a ser pintada :"))

litros = (area_pintar / 3)
lata_litros = 18 
preco_lata = 80

qtd_lata = litros/lata_litros
val_tot = (litros / 18) * 80

print(f"Pintando {area_pintar} metros²\n"
      f"Litros a serem utilizados {litros}L\n"
      f"latas a serem utilizadas {qtd_lata}\n"
      f"Valor total {val_tot}")