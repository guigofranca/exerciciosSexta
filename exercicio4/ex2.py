lista = []

for i in range(3):
    num = int(input("Digite um número: "))
    lista.append(num)
    
print(lista)
print(f"Maior: {max(lista)}")
print(f"Menor: {min(lista)}")