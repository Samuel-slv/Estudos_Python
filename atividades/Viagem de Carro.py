# Entrada de dados
tanque_inicial = float(input("Quantidade inicial de combustivel (litros): "))
tempo_viagem = float(input("Tempo de viagem (horas): "))
consumo_por_hora = float(input("Consumo de combustível por hora (litros/h): "))

# Cálculo
combustivel_restante = tanque_inicial - (tempo_viagem * consumo_por_hora)

# Saída
print(f"Ao final da viagem, restará {combustivel_restante} litros no tanque.")