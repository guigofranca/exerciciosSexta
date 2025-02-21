#Faça um programa que solicite números ao usuário até que ele digite um número negativo.
#Quando isso acontecer, o programa deve exibir a soma de todos os números positivos digitados e encerrar.

lista = []
num = int(input("Digite um número: "))

if num > 0:
    lista.append(num)

while num > 0:
    num = int(input("Digite um número: "))
    
    if num > 0:
        lista.append(num)
    
print("Número negativo digitado!")
print(f"{sum(lista)}")