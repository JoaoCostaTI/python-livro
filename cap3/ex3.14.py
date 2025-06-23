kmPercorrido = int(input('KM percorrido: '))
qtdDias = int(input('Dias: '))
umDia = 60
umKM = 0.15
totalDia = qtdDias * umDia
totalKM = kmPercorrido * umKM

print(f'Valor total devido: R${totalKM + totalDia:.2f}')