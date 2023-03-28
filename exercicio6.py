# Recebe o peso e altura do usuário
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

# Calcula o IMC
imc = peso / altura**2

# Classifica o IMC de acordo com a tabela
if imc < 18.5:
    classificacao = "Pessoa abaixo do peso"
elif imc < 25:
    classificacao = "Pessoa com peso normal"
elif imc < 30:
    classificacao = "Pessoa acima do peso"
else:
    classificacao = "Pessoa obesa"

# Imprime o resultado
print("Seu IMC é: {:.2f}".format(imc))
print(classificacao)