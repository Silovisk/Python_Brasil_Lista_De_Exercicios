def menu():
    print(
    """
    Produto          |   Código |   Preço
    ---------------------------------------
    Cachorro Quente  |   100    |   R$ 1,20
    Bauru Simples    |   101    |   R$ 1,30
    Bauru com ovo    |   102    |   R$ 1,50
    Hambúrguer       |   103    |   R$ 1,20
    Cheeseburguer    |   104    |   R$ 1,30 
    Refrigerante     |   105    |   R$ 1,00
    """
    )
    
resp = True
codigo = preco = quantidade = 0
while resp:
    menu()  
    codigo = int(input("Digite o codigo: "))
    quantidade = int(input("Digite a quantidade: "))

    if(codigo == 100):
        preco += quantidade * 1.20
    elif(codigo == 101):
        preco += quantidade * 1.30
    elif(codigo == 102):
        preco += quantidade * 1.50
    elif(codigo == 103):
        preco += quantidade * 1.20
    elif(codigo == 104):
        preco += quantidade * 1.30
    elif(codigo == 105):
        preco += quantidade * 1.00
    else:
        print("invalido")

    resp = str(input("Digite [y|n] se quiser encerrar o programa: "))
    resp = True if resp == 'n' else False


print(preco)    
