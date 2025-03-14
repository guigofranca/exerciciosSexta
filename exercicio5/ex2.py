import math

def primo(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Digite um número: "))

print(primo(num))
