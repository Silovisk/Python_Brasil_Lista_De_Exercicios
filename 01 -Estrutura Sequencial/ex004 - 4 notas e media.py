total = media = 0

for i in range(4):
    nota = float(input(f"Digite a {i+1}° nota :"))
    total += nota
media = total/4

print(f"Total = {total} \n Media = {media}")