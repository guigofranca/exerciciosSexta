lista = []

for i in range(5):
    num = int(input("Digite um número: "))
    if(num not in lista):
        lista.append(num)
    
print(lista)

