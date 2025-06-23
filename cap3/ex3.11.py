preco = float(input('Preço da mercadoria: '))
desconto = int(input('Desconto: '))
valorFinal = preco - (preco*desconto/100)

print(f'Com {desconto}% de desconto o valor final do produto será: R${valorFinal:.2f}')