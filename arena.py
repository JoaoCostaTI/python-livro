while True:
    tab = int(input('Tabuada de qual numero: [0 Sai] >>> '))

    if tab == 0:
        print("saindo...")
        break
    else:
        for n in range(1, 11):
            print(f'{tab} x {n} = {tab * n}')