area_pintar = float(input("Digite a area ser pintadad em m² :"))

litros = area_pintar/6
litros_lata = 18
litros_galao = 3.6

if (litros%2) != 0:
  litros = litros + 1

qtd_latas = litros/litros_lata
print(qtd_latas)
qtd_galao = litros/litros_galao
qtd_mistu = litros/(qtd_latas+qtd_galao)

if (qtd_latas%2) != 0:
  qtd_latas += 1

if (qtd_galao%2) != 0:
  qtd_galao += 1

print(f"A quantidade em litros e {int(litros)}")
print(f"Comprando apenas latas {int(qtd_latas)} Un")
print(f"Comprando apenas galoes {int(qtd_galao)} Un")
print(f"Comprando misturado {int(qtd_mistu)} Un")