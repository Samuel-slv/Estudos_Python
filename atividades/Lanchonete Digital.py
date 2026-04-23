# Entrada de dados
produto = input("Nome do produto: ")
preco = float(input("Preço unitário: "))
quantidade = int(input("Quantidade comprada: "))

# Cálculo
total = preco * quantidade

# Saída
print(f"Produto foi de rosca: {produto}")
print(f"Valor total da compra: R$ {total}")