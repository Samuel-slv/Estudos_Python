print ("Você é o professr do joão, der 4 notas e faça média dele aparecer!")

nota1 = float(input("1° semestre do joão, foi de: "))
nota2 = float(input("2° semestre a nota, foi de: "))
nota3 = float(input("3° semestre a nota foi de: "))
nota4 = float(input("4° semestre a nota foi de: "))

soma = nota1 + nota2 + nota3 + nota4
resultado = soma / 4

print (f"A nota final do joão é: {resultado:.2f}")