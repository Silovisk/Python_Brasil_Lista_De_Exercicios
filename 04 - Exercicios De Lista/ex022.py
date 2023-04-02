# Criação da lista para armazenar os dados dos mouses
mouses = []

# Loop para coletar as informações dos mouses
while True:
    # Coleta a identificação do mouse
    identificacao = int(input("Digite o número de identificação do mouse (digite 0 para encerrar): "))
    
    # Verifica se o usuário deseja encerrar o programa
    if identificacao == 0:
        break
    
    # Coleta o tipo de defeito do mouse
    defeito = int(input("Digite o tipo de defeito do mouse \n1 - necessita da esfera; \n2 - necessita de limpeza; \n3 - necessita troca do cabo ou conector; \n4 - quebrado ou inutilizado \n"))
    
    if defeito < 1 or defeito > 4:
        print("defeito invalido opçoes de 1 a 4.")
    else:
        # Armazena as informações do mouse na lista
        mouses.append((identificacao, defeito))

'''
# Cálculo da quantidade e percentual de cada situação de defeito
quantidade_esfera = sum([1 for mouse in mouses if mouse[1] == 1])
percentual_esfera = quantidade_esfera / len(mouses) * 100

quantidade_limpeza = sum([1 for mouse in mouses if mouse[1] == 2])
percentual_limpeza = quantidade_limpeza / len(mouses) * 100

quantidade_cabo = sum([1 for mouse in mouses if mouse[1] == 3])
percentual_cabo = quantidade_cabo / len(mouses) * 100

quantidade_quebrado = sum([1 for mouse in mouses if mouse[1] == 4])
percentual_quebrado = quantidade_quebrado / len(mouses) * 100
'''

# Cálculo da quantidade e percentual de cada situação de defeito
quantidades = [0, 0, 0, 0]
for mouse in mouses:
    quantidades[mouse[1]-1] += 1

percentuais = [quantidade / len(mouses) * 100 for quantidade in quantidades]

# Impressão do relatório
print("Quantidade de mouses:", len(mouses))
print()
print("Situação                               Quantidade              Percentual")
print("1- necessita da esfera                 ", quantidade_esfera, " " * (21 - len(str(quantidade_esfera))), round(percentual_esfera), "%")
print("2- necessita de limpeza                ", quantidade_limpeza, " " * (21 - len(str(quantidade_limpeza))), round(percentual_limpeza), "%")
print("3- necessita troca do cabo ou conector ", quantidade_cabo, " " * (21 - len(str(quantidade_cabo))), round(percentual_cabo), "%")
print("4- quebrado ou inutilizado             ", quantidade_quebrado, " " * (21 - len(str(quantidade_quebrado))), round(percentual_quebrado), "%")
