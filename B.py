estoque = {
    'Tomate': [1000, 2.30],
    'Alface': [500, 0.45],
    'Batata': [2001, 1.20],
    'Feijão': [100, 1.50],
}
#armazenar e organizar informações utilizando uma estrutura: chave / valor
total = 0
#definindo a váriavel "total" como 0
print("Vendas:\n")
while True:
    produto = input("Nome do produto (fim para sair):")
    if produto == "fim":
        break
    #estrutura enquanto definida verdadeira enquanto a pessoa não digitar "fim"
    if produto in estoque:
        quantidade = int(input("Quantidade:"))
    #verificando se o produto está no estoque
        if quantidade <= estoque[produto][0]:
            preço = estoque[produto][1]
            custo = preço * quantidade
            print(f"{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2f}")
            estoque[produto][0] -= quantidade
            total += custo
        #definições dos produtos do estoque
        else:
            print("Quantidade solicitada não disponível")
        #senão, caso a quantidade solicitada não esteja disponível
    else:
        print("Nome de produto inválido")
        print(f" Custo total: {total:21.2f}\n")
        print("Estoque:\n")
    for chave, dados in estoque.items():
        print("Descrição: ", chave)
        print("Quantidade: ", dados[0])
        print(f"Preço: {dados[1]:6.2f}\n")
