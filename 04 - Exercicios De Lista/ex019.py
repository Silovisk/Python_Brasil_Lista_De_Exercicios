def calcular_percentual_votos(votos_sistema, total_votos):
    return (votos_sistema / total_votos) * 100

opcoes = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
votos = [0] * 6

menu = """
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
0- Sair.."""

while True:
    voto = int(input(f'{menu}\nDigite o número da opção desejada (0 para encerrar): '))
    if voto == 0:
        break
    elif voto >= 1 and voto <= 6:
        votos[voto-1] += 1
    else:
        print('Opção inválida! Digite um número entre 0 e 6.')

total_votos = sum(votos)
print('Sistema Operacional\tVotos\t%')
print('-'*25)
for i in range(len(opcoes)):
    print(f'{opcoes[i]:<20}{votos[i]:<8}{calcular_percentual_votos(votos[i],total_votos):.2f}%')
print('-'*25)
print(f'Total\t\t\t{total_votos}\n')

indice_vencedor = votos.index(max(votos))
print(f'O Sistema Operacional mais votado foi o {opcoes[indice_vencedor]} com {votos[indice_vencedor]} votos, correspondendo a {(votos[indice_vencedor]/total_votos*100):.0f}% dos votos.')
