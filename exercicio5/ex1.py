def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Digite um número: "))

print(factorial(num))

