import statistics

def mediaV(lista):
    return statistics.mean(lista)

lista = []

tamanho = int(input("Digite o tamanho da lista: "))

for i in range(tamanho):
    num = int(input("Digite os valores da lista: "))
    lista.append(num)

print(mediaV(lista))