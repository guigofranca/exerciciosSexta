#Faça um programa que pergunte o número de horas trabalhadas no mês e o valor recebido
#por hora. O programa deve calcular e exibir o salário total do mês.

horas = float(input("Quantas horas trabalhadas no mês?"))
valor = float(input("Qual o valor recebido por hora?"))

total = horas/valor
print(f"Salário total do mês: {total}")