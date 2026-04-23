temperatura = float(input("Digite a temperatura em Celsius: "))

if temperatura < 10:
    classificacao = "Muito frio"
elif temperatura < 20:
    classificacao = "Frio"
elif temperatura < 30:
    classificacao = "Agradável"
else:
    classificacao = "Quente"

print(f"A classificação final é: {classificacao}")