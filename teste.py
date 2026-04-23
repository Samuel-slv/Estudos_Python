# Variável para armazenar o resumo das escolhas
pedido_final = ""

print("===== SISTEMA DE PEDIDOS =====")

while True:
    print("\nCATEGORIAS:")
    print("1 - Entradas")
    print("2 - Pratos Principais")
    print("3 - Bebidas")
    print("4 - Finalizar e Ver Resumo")
    
    categoria = input("\nEscolha a categoria (1-4): ")

    if categoria == "4":
        break  # Sai do loop while
    
    elif categoria == "1":
        print("\nENTRADAS: 1.Batata Frita | 2.Anéis de Cebola | 3.Coxinha | 4.Pastel | 5.Pão de Alho")
        item = input("Opção desejada: ")
        qtd = input("Quantas porções? ")
        
        if item == "1": nome = "Batata Frita"
        elif item == "2": nome = "Anéis de Cebola"
        elif item == "3": nome = "Coxinha"
        elif item == "4": nome = "Pastel"
        else: nome = "Pão de Alho"
        
        pedido_final += f"{qtd}x {nome}\n"

    elif categoria == "2":
        print("\nPRATOS: 1.Strogonoff | 2.Feijoada | 3.Lasanha | 4.Peixe | 5.Hambúrguer")
        item = input("Opção desejada: ")
        qtd = input("Quantas porções? ")
        
        if item == "1": nome = "Strogonoff"
        elif item == "2": nome = "Feijoada"
        elif item == "3": nome = "Lasanha"
        elif item == "4": nome = "Peixe"
        else: nome = "Hambúrguer"
        
        pedido_final += f"{qtd}x {nome}\n"

    elif categoria == "3":
        print("\nBEBIDAS: 1.Refrigerante | 2.Suco | 3.Água | 4.Cerveja | 5.Café")
        item = input("Opção desejada: ")
        qtd = input("Quantas unidades? ")
        
        if item == "1": nome = "Refrigerante"
        elif item == "2": nome = "Suco"
        elif item == "3": nome = "Água"
        elif item == "4": nome = "Cerveja"
        else: nome = "Café"
        
        pedido_final += f"{qtd}x {nome}\n"
    
    else:
        print("Opção inválida! Tente novamente.")

# Saída final apresentando as escolhas
print("\n" + "="*30)
print("RESUMO DO SEU PEDIDO:")
if pedido_final == "":
    print("Nenhum item foi selecionado.")
else:
    print(pedido_final)
print("="*30)