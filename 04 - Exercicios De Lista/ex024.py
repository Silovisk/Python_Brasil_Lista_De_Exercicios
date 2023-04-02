from random import randint

contadores = [0] * 6

for i in range(100):
    resultado = randint(1, 6)
    contadores[resultado-1] += 1

for i in range(6):
    print("Número de vezes que a face", i+1, "foi obtida:", contadores[i])
