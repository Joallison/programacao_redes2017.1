frase = input('Digite a frase: ')
caractere = input ('Digite o caractre: ')

def cont(a, b):
    contador = 0;
    for x in a:
        if x == b:
            contador = contador + 1
    return contador
    
print(cont(frase,caractere))
