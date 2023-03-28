mensagem_criptografada = ['8', '5', '-1', '7', '6', '-1', '8', '4', '-1', '7', '3', '-1', '7', '7', '-1', '6', '5', '-1']

palavra = ''
codigo_letra = ''

for codigo in mensagem_criptografada:
    if codigo == '-1':
        palavra += chr(int(codigo_letra))
        codigo_letra = ''
    else:
        codigo_letra += codigo

print(palavra)