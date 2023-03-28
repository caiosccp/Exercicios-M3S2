altura = float(input("Qual é a sua altura em metros? "))
genero = input("Você é homem ou mulher? ")

if genero.lower() == "homem":
    peso_ideal = round((72.7 * altura) - 58, 2)
    print(f"Você é homem e seu peso ideal é de {peso_ideal} kg.")
elif genero.lower() == "mulher":
    peso_ideal = round((62.1 * altura) - 44.7, 2)
    print(f"Você é mulher e seu peso ideal é de {peso_ideal} kg.")
else:
    print("Gênero inválido. Por favor, informe 'homem' ou 'mulher'.")