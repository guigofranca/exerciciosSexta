#Escreva um programa que peça um número inteiro positivo ao usuário e exiba todos os
#números de 1 até esse número, um por linha.

num = int(input("Digite um número: "))

for i in range (num):
    print(f"{i + 1}")