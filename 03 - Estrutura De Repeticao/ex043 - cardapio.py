"""
O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
Considere que o cliente deve informar quando o pedido deve ser encerrado.

"""
b
print(f"""
-----------  CARDAPIO -----------
Especificação   Código    Preço
________________________________
Cachorro Quente  100     R$ 1,20
Bauru Simples    101     R$ 1,30
Bauru com ovo    102     R$ 1,50
Hambúrguer       103     R$ 1,20
Cheeseburguer    104     R$ 1,30
Refrigerante     105     R$ 1,00
""")
valor_pagar = 0
resp = True
while resp == True:
    codigo = int(input("Informe um codigo: "))
    qtd = int(input("Informe a quantidade: "))

    match codigo:
        case 100:
            preco = 1.20
        case 101:
            preco = 1.30
        case 102:
            preco = 1.50
        case 103:
            preco = 1.20
        case 104:
            preco = 1.30
        case 105:
            preco = 1.00
    
    valor_pagar += qtd * preco

    rep = input("Deseja encerrar o pedido: [y/n]")
    resp = True if rep == "n" else False

print("Pedido encerrado...")

print(f"""
------------  RECIBO -----------
Total a pagar :   R$ {valor_pagar}
________________________________
""")
