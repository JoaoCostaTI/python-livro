import time
agora = time.localtime()

print(agora)

print(f"Ano: {agora.tm_year}")
print(f"Mês: {agora.tm_mon}")
print(f"Dia: {agora.tm_wday}")
print(f"Hora: {agora.tm_hour}")
print(f"Minuto: {agora.tm_min}")
print(f"Segundos: {agora.tm_sec}")
print(f"Dia da Semana: {agora.tm_wday}")
print(f"Dia do ano: {agora.tm_yday}")
print(f"Horário de verão [[1] = Horário de verão ativo] : {agora.tm_isdst} ")



