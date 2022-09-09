qtd_notas = int(input("Digite o numero de notas que deseja inserir: "))
soma = media = 0
c = 1
while c <= qtd_notas:
    notas = float(input(f"Digite o valor da {c}° nota: "))
    soma += notas
    c += 1
media = soma / qtd_notas

print(f"\nQuantidade de notas = {qtd_notas}\nSoma = {soma} \nMedia = {media}")