# Criando o dicionário com os valores dos usuários
usuarios = {
    'alexandre': 456123789,
    'anderson': 1245698456,
    'antonio': 123456456,
    'carlos': 91257581,
    'cesar': 987458,
    'rosemary': 789456125
}

# Função para converter bytes em megabytes
def converte_bytes_para_megabytes(bytes):
    megabytes = bytes / 1024 / 1024
    return megabytes

# Função para calcular o percentual de uso
def calcula_percentual_uso(espaco_utilizado, espaco_total):
    percentual = (espaco_utilizado / espaco_total) * 100
    return percentual

# Convertendo e somando o espaço utilizado pelos usuários
espaco_total = 0
for usuario in usuarios:
    espaco_utilizado = converte_bytes_para_megabytes(usuarios[usuario])
    usuarios[usuario] = espaco_utilizado
    espaco_total += espaco_utilizado

# Criando a lista de usuários ordenada pelo espaço utilizado
usuarios_ordenados = sorted(usuarios.items(), key=lambda x: x[1], reverse=True)

# Gerando o relatório
print('ACME Inc.               Uso do espaço em disco pelos usuários')
print('-' * 70)
print('Nr.  Usuário        Espaço utilizado     % do uso\n')

contador = 1
for usuario in usuarios_ordenados:
    espaco_utilizado = usuario[1]
    percentual_uso = calcula_percentual_uso(espaco_utilizado, espaco_total)
    print(f'{contador:<4} {usuario[0]:<15} {espaco_utilizado:>15.2f} MB {percentual_uso:>14.2f}%')
    contador += 1

espaco_medio = espaco_total / len(usuarios)
print(f'\nEspaço total ocupado: {espaco_total:.2f} MB')
print(f'Espaço médio ocupado: {espaco_medio:.2f} MB')
