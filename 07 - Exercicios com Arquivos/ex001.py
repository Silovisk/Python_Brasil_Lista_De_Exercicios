import socket

def validar_ip(endereco_ip):
    try:
        # Verifica se o endereço IP está no formato correto
        socket.inet_aton(endereco_ip)
        
        # Verifica se o endereço IP está dentro do intervalo correto
        octetos = endereco_ip.split('.')
        if len(octetos) != 4:
            return False
        if int(octetos[0]) == 10:
            return True
        if int(octetos[0]) == 172 and 16 <= int(octetos[1]) <= 31:
            return True
        if int(octetos[0]) == 192 and int(octetos[1]) == 168:
            return True
        
        return False
    except socket.error:
        return False

# Define o nome do arquivo de entrada e de saída
arquivo_entrada = '07 - Exercicios com Arquivos\ex001\ex001.txt'
arquivo_saida = '07 - Exercicios com Arquivos\ex001\\relatorio.txt'

# Abre o arquivo de entrada para leitura e o arquivo de saída para escrita
with open(arquivo_entrada, 'r') as f_in, open(arquivo_saida, 'w', encoding='utf-8') as f_out:

    # Inicializa as listas para armazenar os endereços válidos e inválidos
    enderecos_validos = []
    enderecos_invalidos = []

    # Percorre cada linha do arquivo de entrada
    for linha in f_in:

        # Remove o caractere de quebra de linha do final da linha
        linha = linha.rstrip()

        # Valida o endereço IP
        if validar_ip(linha):
            enderecos_validos.append(linha)
        else:
            enderecos_invalidos.append(linha)

    # Escreve os endereços válidos e inválidos no arquivo de saída
    f_out.write('[Endereços válidos:]\n')
    for endereco in enderecos_validos:
        f_out.write(endereco + '\n')

    f_out.write('\n[Endereços inválidos:]\n')
    for endereco in enderecos_invalidos:
        f_out.write(endereco + '\n')
