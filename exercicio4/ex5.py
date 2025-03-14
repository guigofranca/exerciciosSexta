lista = []

numE = int(input("Digite o número específico: "))

x = 0

for i in range(3):
    num = int(input("Digite um número: "))
    if num == numE:
        x =+ 1
    lista.append(num)
    
print(lista)

print(f"Total de número repetido: {x}")