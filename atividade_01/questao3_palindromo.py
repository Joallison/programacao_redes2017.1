palavra = input('Digite uma palavra:  ')

if palavra==palavra[::-1]:
    print('A palavra é palíndromo --> %s'%(palavra))
else:
    print('A frase não é palíndromo --> %s'%(palavra))
