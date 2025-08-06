def fib(n):
    valor = 0
    if n == 0 or n == 1:
        return n
    else:
        fibo = fib(n - 1) + fib(n - 2)
        valor += fibo
    
    return valor

print(fib(8))