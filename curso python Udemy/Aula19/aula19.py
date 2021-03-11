'''
fatiamento de strings com python
'''
nome = 'Jose Dembo'
vetor = [[10, 20, 30], 1, 4, 5, 7]
print(nome[:5])

print(vetor[0][1:]) # pega o primeiro elemeto do vetor(outro vetor),
# e ai pega novamente do segundo ao último elemento

print(nome[::2]) # os '::' servem quando queremos pular elementos, indicando os espaços

n = []
b = 0
for letra in nome:
    if letra == ' ':
            b = 1
    if b == 0 :
        n.append(letra)

