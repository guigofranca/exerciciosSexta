def conta_vogais(string):
    contador = 0
    vogais = 'aeiouAEIOU'
    for i in vogais:
        if i in string:
            contador += 1
            
    return contador

string = input("Digite uma palavra: ")

print(conta_vogais(string))