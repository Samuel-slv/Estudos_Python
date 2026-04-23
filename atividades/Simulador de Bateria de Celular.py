carga = float(input("Carga inicial da bateria: "))
consumo_hora = float(input("Consumo por hora: "))
recuperacao_hora = float(input("Recuperação por hora: "))

horas_completas = 0
# O consumo real por hora é a diferença entre gasto e recuperação
consumo_real = consumo_hora - recuperacao_hora

while carga >= consumo_real and consumo_real > 0:
    carga -= consumo_real
    horas_completas += 1

print(f"\nO celular funcionou por {horas_completas} horas completas.")
print(f"Restou {carga:.2f} de bateria antes de desligar.")
