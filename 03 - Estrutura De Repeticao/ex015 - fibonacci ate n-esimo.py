n_esimo = int(input("Digite o n-esimo termo:"))

ultimo = 0
primeiro = 0
segundo = 1

print(segundo)
for i in range(n_esimo):  
  ultimo = primeiro + segundo
  primeiro = segundo
  segundo = ultimo
  print(ultimo)