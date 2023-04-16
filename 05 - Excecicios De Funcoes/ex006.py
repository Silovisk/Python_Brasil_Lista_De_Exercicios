def converter_horario(hora, minuto):
    if hora == 0:
        hora_formatada = 12
        periodo = 'A'
    elif hora < 12:
        hora_formatada = hora
        periodo = 'A'
    elif hora == 12:
        hora_formatada = 12
        periodo = 'P'
    else:
        hora_formatada = hora - 12
        periodo = 'P'
    return hora_formatada, minuto, periodo

def imprimir_horario(hora_formatada, minuto, periodo):
    print(f"{hora_formatada}:{minuto} {periodo}.M.")

while True:
    hora = int(input("Digite a hora (0-23): "))
    minuto = int(input("Digite o minuto (0-59): "))

    hora_formatada, minuto_formatado, periodo = converter_horario(hora, minuto)
    imprimir_horario(hora_formatada, minuto_formatado, periodo)

    opcao = input("Deseja converter outro horário? (s/n) ")
    if opcao.lower() == "n":
        break
