#Peça ao usuário dois números inteiros, representando um intervalo A,B. O programa deve
#exibir todos os números ímpares dentro desse intervalo (inclusive os limites, se forem ímpares).

num1 = int(input("Digite um número: "))

num2 = int(input("Digite outro número: "))

if num1 > num2:
    num1, num2 = num2, num1

for num1 in range(num2):
    if num1%2 != 0:
        print(num1)
    num1 = num1 + 1