def fibonacci(n: int) -> int:
    if n <= 0:
        return "Por favor, insira um número positivo!"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Testando a função
n = int(input("Digite o valor de N: "))
print(f"O {n}-ésimo número da sequência de Fibonacci é: {fibonacci(n)}")