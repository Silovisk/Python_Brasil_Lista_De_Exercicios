multa = 4.00 
max_quilos = 50
valor_total = 0
peso_peixes = float(input("Digite o peso de peixes pegos :"))

if peso_peixes > max_quilos:
  total_excedente = peso_peixes - max_quilos
  valor_total = total_excedente * multa

print(f"O valor total a se pagar e {valor_total}")