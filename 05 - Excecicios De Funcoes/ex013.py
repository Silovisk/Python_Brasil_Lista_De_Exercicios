def desenha_moldura(linhas=1, colunas=1):
    # Ajusta os valores de linhas e colunas para ficarem dentro da faixa de 1 a 20
    linhas = max(1, min(20, linhas))
    colunas = max(1, min(20, colunas))
    
    # Desenha a moldura
    for i in range(linhas):
        if i == 0 or i == linhas-1:
            print('+' + '-'*(colunas-2) + '+')
        else:
            print('|' + ' '*(colunas-2) + '|')

desenha_moldura(20,20)