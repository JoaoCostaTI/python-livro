pessoas = [
    {"id": 1, "nome": "Ana Silva",         "registro": 1045123789},
    {"id": 2, "nome": "Bruno Castro",      "registro": 1056234987},
    {"id": 3, "nome": "Carla Mendes",      "registro": 1067345123},
    {"id": 4, "nome": "Daniel Rocha",      "registro": 1078456234},
    {"id": 5, "nome": "Elaine Ferreira",   "registro": 1089567345},
    {"id": 6, "nome": "Fábio Lima",        "registro": 1090678456},
    {"id": 7, "nome": "Gabriela Souza",    "registro": 1011789567},
    {"id": 8, "nome": "Henrique Alves",    "registro": 1022890678},
    {"id": 9, "nome": "Isabela Duarte",    "registro": 1033901789},
    {"id": 10,"nome": "João Pires",        "registro": 1044012890},
    {"id": 11,"nome": "Karen Moreira",     "registro": 1055123901},
    {"id": 12,"nome": "Lucas Matos",       "registro": 1066234012},
    {"id": 13,"nome": "Marcela Antunes",   "registro": 1077345123},
    {"id": 14,"nome": "Nathan Oliveira",   "registro": 1088456234},
    {"id": 15,"nome": "Otávio Costa",      "registro": 1099567345},
]


print('-' * 50)
print(f'{"ID":<5}{"Nome":<20}{"Registro":<20}')
print('-' * 50)

for pessoa in pessoas:
    print(f'{pessoa["id"]:<5}{pessoa["nome"]:<20}{pessoa["registro"]:<20}')

