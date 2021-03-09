'''
isnumeric, isdigit, isdecimal (metodos de String) :
essas funções verificam se o usuaario digiou um numero POSITIVO SEM PONTO FLUTUANTE
'''
num1 = input('digiteum numero ')
num2 = input('digite outro numero ')

teste1 = num1.isnumeric()
teste2 = num2.isnumeric()

try:
    if teste1:
        num1 = int(num1)
        if teste2:
            num2 = int(num2)
        else:
            print('O segundo valor digitado nao e um numero')
            exit()
    else:
        print('O primeiro valor digtado nao e um numero')
        exit()

    resultado = num1 + num2

    print(f'A soma entre {num1} e {num2} é: {resultado}')
except:
    print('ERROR')


