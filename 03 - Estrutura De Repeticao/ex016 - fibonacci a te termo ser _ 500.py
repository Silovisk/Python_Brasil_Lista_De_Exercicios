primeiro = 0
segundo = 1
ultimo = 0

i = 0

print(segundo)
while i != 1:
  ultimo = primeiro + segundo
  primeiro = segundo
  segundo = ultimo
  print(ultimo)
  if ultimo > 500:
    i = 1