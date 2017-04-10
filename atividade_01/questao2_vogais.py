palavra = input('Digite a palavra: ')
vogais = 'aeiou'

def buscavogais(a, b):
    contvogais = 0;
    for x in a:
        if x in b:
            contvogais = contvogais + 1
    return contvogais

print(buscavogais(palavra,vogais))
