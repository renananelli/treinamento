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

# Testes com pytest
def test_fibonacci_com_valores_negativos():
    assert fibonacci(0) == "Por favor, insira um número positivo!"

def test_fibonacci_para_n_igual_1():
    assert fibonacci(1) == 0

def test_fibonacci_para_n_igual_2():
    assert fibonacci(2) == 1

def test_fibonacci_para_n_igual_3():
    assert fibonacci(3) == 1

def test_fibonacci_para_n_igual_4():
    assert fibonacci(4) == 2

def test_fibonacci_para_n_igual_5():
    assert fibonacci(5) == 3

def test_fibonacci_para_n_igual_10():
    assert fibonacci(10) == 34
