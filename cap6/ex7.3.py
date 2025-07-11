s1 = 'CTA'
s2 = 'ABC'
s3 = ''

for letra in s1:
    if letra not in s2:
        s3 += letra
for letra in s2:
    if letra not in s1:
        s3 += letra
print(s3)

primeira = 'CTA'
segunda = 'ABC'

terceira = ""

# Para cada letra na primeira string
for letra in primeira:
    # Verifica se a letra não aparece dentro da segunda string
    # e também se já não está listada na terceira
    if letra not in segunda and letra not in terceira:
        terceira += letra

# Para cada letra na segunda string
for letra in segunda:
    # Além de não estar na primeira string,
    # verifica se já não está na terceira (evitar repetições)
    if letra not in primeira and letra not in terceira:
        terceira += letra

if terceira == "":
    print("Caracteres incomuns não encontrados.")
else:
    print(f"Caracteres incomuns: {terceira}")