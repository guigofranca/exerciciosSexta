#Peça um número inteiro ao usuário e exiba a tabuada desse número de 1 a 10.

num = int(input("Digite um número para fazer a tabuada: "))

i = 1

while i < 11:
    tabuada = num * i
    print(f"{tabuada}")
    i = i + 1