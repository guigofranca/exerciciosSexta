#Faça um programa que peça dois números ao usuário e exiba o maior deles. Caso os números
#sejam iguais, exiba uma mensagem informando essa condição.

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

lista = []

lista.append(num1)
lista.append(num2)

if num1 == num2:
    print("são iguais")
else:
    print(f"maior número: {max(lista)}")