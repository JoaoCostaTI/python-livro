def fib(n):
    print(f'Calculando Fibonacci de {n}')
    if n <= 1:
        print(f'Fibonacci de {n} = {n}')
        return n
    else:
        print(f'Fibonacci de {n} = fibonacci {n-1} + fibonacci {n-2} = ...')
        resultado = fib(n-1) + fib(n-2)
        print(f'Fibonacci de {n} = fibonacci {n-1} + fibonacci {n-2} = {resultado}')
        return resultado
print(fib(5))