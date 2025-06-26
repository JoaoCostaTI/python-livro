quantidade_de_primos = int(input("Digite a quantidade de números primos a gerar: "))
if quantidade_de_primos < 0:
    print("Número inválido. Digite apenas valores positivos")
else:
    if quantidade_de_primos >= 1:
        print("2")  # 2 é o único número que é primo e par ao mesmo tempo
    primos_gerados = 1  # logo é o primeiro número primo gerado
    próximo_primo = 3  # o próximo primo começa então com 3
    while primos_gerados < quantidade_de_primos:
        # Como todos os primos seguintes são ímpares
        divisor = 3
        while divisor < próximo_primo:
            # Se o resto for zero, o número é divisível
            if próximo_primo % divisor == 0:
                break
            # Incrementa o divisor
            divisor = divisor + 2
        # Quando o número é primo, ele é divisível apenas por ele mesmo
        if divisor == próximo_primo:
            print(próximo_primo)
            primos_gerados = primos_gerados + 1
        # passa para o próximo número ímpar,
        # pois os pares não são primos, salvo 2
        próximo_primo = próximo_primo + 2