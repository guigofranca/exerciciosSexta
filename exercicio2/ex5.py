#Peça ao usuário três números representando os lados de um triângulo. O programa deve
#verificar e informar se os valores formam um triângulo válido (a soma de dois lados deve ser
#sempre maior que o terceiro).

lado1 = int(input("Lado 1: "))
lado2 = int(input("Lado 2: "))
lado3 = int(input("Lado 3: "))

if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1:
    print("Triângulo válido!")
else:
    print("Inválido")