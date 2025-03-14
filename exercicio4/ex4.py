#Escreva um programa que leia uma lista de palavras e exiba essa lista na ordem inversa.
lista = []

for i in range(3):
    palavras = input("Digite uma palavra: ")
    lista.append(palavras)
    
print(lista)
lista.reverse()
print(lista)
