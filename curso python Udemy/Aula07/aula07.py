'''
formatação de Strings
'''
nome = 'José'
idade = 21
peso = 84.7
altura = 1.80
IMC = peso/altura**2
print('Nome:', nome, '\nidade:',idade, '\naltura:', altura,'\nIndice de massa corporal(IMC):', IMC)
print(f'Nome:{nome}, idade:{idade}, altura:{altura}, IMc:{IMC:.2f}')
print(f'{nome}, tem {idade} anos, seu IMC é {IMC:.2f}')
print('{} tem {} anos de idade, seu IMC é {:.3f} '.format(nome, idade, IMC))
print('{0} tem {1} anos de idade, seu IMC é {2:.3f} '.format(nome, idade, IMC))
print('{n} tem {i} anos de idade, seu IMC é {im:.3f} mais {im}'.format(n=nome, i=idade, im=IMC))