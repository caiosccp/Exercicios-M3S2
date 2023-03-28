deslocamento = 3
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dicionario = {}
for i, letra in enumerate(alfabeto):
    nova_letra = alfabeto[(i + deslocamento) % len(alfabeto)]
    dicionario[nova_letra] = letra

mensagem_criptografada = 'HVWRX HPSROJDGR FRP R FXUVR GH SBWKRQ'
mensagem_descriptografada = ''
for letra in mensagem_criptografada:
    if letra == ' ':  # não aplicamos deslocamento para o caractere espaço
        mensagem_descriptografada += letra
    else:
        mensagem_descriptografada += dicionario[letra]

print(mensagem_descriptografada)