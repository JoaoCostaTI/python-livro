import sys

print(f"Numeo de parametros: {len(sys.argv)}")
for n, p in enumerate(sys.argv):
    print(f"Parametro {n} = {p}")
