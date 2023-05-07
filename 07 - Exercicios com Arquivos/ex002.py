def converter_bytes_megabytes(bytes) -> float:
    megabytes = bytes /  1000000
    return megabytes

def percentual_uso(bytes, total):
    percentual = (bytes / total) * 100
    return percentual

arquivo_entrada = r'07 - Exercicios com Arquivos\ex002\usuarios.txt'
arquivo_saida = r'07 - Exercicios com Arquivos\ex002\relatório.txt'

usuarios = {}
soma_total = 0
percentual = 0

with open(arquivo_entrada, 'r') as f_in:
    for linha in f_in:
        linha = linha.strip()
        nome, numero_by = linha.split()
        usuarios[nome] = int(numero_by)

    soma_total = sum(usuarios.values())

with open(arquivo_saida, 'w', encoding='utf-8') as f_out:
    f_out.write('ACME Inc.               Uso do espaço em disco pelos usuários\n')
    f_out.write('-----------------------------------------------------------------------\n')
    f_out.write('Nr.  Usuário        Espaço utilizado     % do uso\n\n')

    numero_usuario = 1
    for nome, numero_by in usuarios.items():
        espaco_utilizado_mb = converter_bytes_megabytes(numero_by)
        percentual_de_uso = percentual_uso(numero_by, soma_total)
        f_out.write(f'{numero_usuario:<4} {nome:<15} {espaco_utilizado_mb:>10.2f} MB        {percentual_de_uso:>5.2f}%\n')
        numero_usuario += 1

    espaco_total_mb = converter_bytes_megabytes(soma_total)
    espaco_medio_mb = espaco_total_mb / len(usuarios)
    f_out.write(f'\nEspaço total ocupado: {espaco_total_mb:.2f} MB\n')
    f_out.write(f'Espaço médio ocupado: {espaco_medio_mb:.2f} MB\n')

