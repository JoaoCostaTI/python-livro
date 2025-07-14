s1 = 'AAACTBF'
s2 = 'CBT'
terceira = ""

for letra in s1:
    if letra not in terceira and letra in s2:
        terceira += letra
print(terceira)