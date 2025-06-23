"""
dias = int(input('Dias: '))
segundos = dias * 24 * 60 * 60
hora = int(input('Horas: '))
segundos += hora * 60 * 60
minutos = int(input('Minutos: '))
segundos += minutos * 60
segundosUsuario = int(input('Segundos: '))
segundos += segundosUsuario

print(f'Total em segundos: {segundos}')
"""
dias = int(input("Dias:"))
horas = int(input("Horas:"))
minutos = int(input("Minutos:"))
segundos = int(input("Segundos:"))
# Um minuto tem 60 segundos
# Uma hora tem 3600 (60 * 60) segundos
# Um dia tem 24 horas, logo 24 * 3600 segundos
total_em_segundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos
print("Convertido em segundos é igual a %10d segundos." % total_em_segundos)
