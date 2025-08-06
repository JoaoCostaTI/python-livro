a = 5

def mudaEimprime():
    global a
    a = 7
    print(f"Dentro da função : {a}")
print(f'Antes de mudar: {a}')
mudaEimprime()
print(f'Depois de mudar : {a}')