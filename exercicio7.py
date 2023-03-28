# Recebe o valor de etiqueta e a forma de pagamento
valor_etiqueta = float(input("Digite o valor de etiqueta do produto: "))
forma_pagamento = int(input("Digite a forma de pagamento (1 - À vista em dinheiro, 2 - À vista no cartão de crédito, 3 - Em duas vezes, 4 - Mais de duas vezes): "))

# Calcula o preço final de acordo com a forma de pagamento
if forma_pagamento == 1:
    preco_final = valor_etiqueta * 0.85
elif forma_pagamento == 2:
    preco_final = valor_etiqueta * 0.9
elif forma_pagamento == 3:
    preco_final = valor_etiqueta
elif forma_pagamento == 4:
    preco_final = valor_etiqueta * 1.1
else:
    print("Forma de pagamento inválida.")
    preco_final = 0

# Imprime o preço final
if preco_final > 0:
    print("Preço final: R$ {:.2f}".format(preco_final))