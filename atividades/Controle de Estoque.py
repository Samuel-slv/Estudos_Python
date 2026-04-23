capacidade_maxima = int(input("Capacidade máxima do estoque: "))

total_itens = 0
entregas_feitas = 0

while True:
    entrega = int(input("Quantidade de itens da entrega (ou 0 para sair): "))
    
    if entrega == 0:
        break # Para o loop
        
    total_itens += entrega
    entregas_feitas += 1

# Quantas vezes o estoque seria preenchido (divisão inteira)
vezes_preenchido = total_itens // capacidade_maxima

print(f"\nTotal de itens recebidos: {total_itens}")
print(f"Total de entregas feitas: {entregas_feitas}")
print(f"O estoque seria preenchido {vezes_preenchido} vezes.")