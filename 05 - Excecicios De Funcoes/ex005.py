def somaimposto(taxaimposto, custo):
    resultado = custo - taxaimposto
    return resultado

custo_produto = float(input("Digite o custo do produto: "))
quantia_imposto = float(input("Digite a taxa de imposto: "))

novo_preco = somaimposto(quantia_imposto, custo_produto)

print(f"O novo preço e R$ {novo_preco:.2f}")