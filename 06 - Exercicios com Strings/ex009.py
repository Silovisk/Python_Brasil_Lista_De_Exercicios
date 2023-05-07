def validar_cpf(cpf):
    # Remove os caracteres de formatação
    cpf = cpf.replace(".", "").replace("-", "")
    
    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os caracteres são iguais
    if cpf == cpf[0] * 11:
        return False
    
    # Verifica se o CPF é válido
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    digito_1 = 11 - (soma % 11)
    if digito_1 > 9:
        digito_1 = 0
    if digito_1 != int(cpf[9]):
        return False
    
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    digito_2 = 11 - (soma % 11)
    if digito_2 > 9:
        digito_2 = 0
    if digito_2 != int(cpf[10]):
        return False
    
    # Se chegou até aqui, o CPF é válido
    return True

cor_verde = "\033[32m"
cor_vermelha = "\033[31m"
reset_cor = "\033[0m"

cpfs = [
    '864.464.227-84',
    '236.073.246-68',
    '546.426.789-43',
    '332.249.168-19',
    '047.070.253-87',
    '111.111.111-11',
    '222.222.222-22',
    '333.333.333-33',
    '444.444.444-44',
    '555.555.555-55',
    '012.345.678-90',    
    '111.444.777-35',    
    '529.982.247-25',    
    '584.963.175-03',    
    '784.230.196-40',    
    '920.478.736-02'
]


for i in range(len(cpfs)):
    if validar_cpf(cpfs[i]):
        print(f"{cor_verde}{cpfs[i]}{reset_cor}")
    else:
        print(f"{cor_vermelha}{cpfs[i]}{reset_cor}")
