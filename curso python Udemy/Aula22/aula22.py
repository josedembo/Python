'''
Iterando Strings com while
o rato roeu a roupa do rei de roma
'''
frase = input('Informe o seu nome completo: ')
tamanho_frase = len(frase)
print(tamanho_frase)
nova_frase = ''
contador = 0

input_do_usuario = input('Informe qual letra deseja colocar maiúscula')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_frase = nova_frase + letra.upper()
    else:
        nova_frase = nova_frase + frase[contador]
    contador += 1
print(nova_frase)


'''
contador = tamanho_frase - 1
while contador > 0:
    if frase[contador] == ' ':
        cont = contador +1
        while True:
            sobrenome += frase[cont]
            cont += 1
            if cont == tamanho_frase:
                break
    contador -= 1
print(f'Prazer em conhece-lo sr(a) {sobrenome}')
'''