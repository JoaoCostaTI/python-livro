from estados import Estados
from cidade import Cidade

# Populações obtidas no site da Wikipédia
# IBGE estimativa 2012
am = Estados("Amazonas", "AM")
am.adicionaCidade(Cidade("Manaus", 1861838))
am.adicionaCidade(Cidade("Parintins", 103828))
am.adicionaCidade(Cidade("Itacoatiara", 89064))

sp = Estados("São Paulo", "SP")
sp.adicionaCidade(Cidade("São Paulo", 11376685))
sp.adicionaCidade(Cidade("Guarulhos", 1244518))
sp.adicionaCidade(Cidade("Campinas", 1098630))

rj = Estados("Rio de Janeiro", "RJ")
rj.adicionaCidade(Cidade("Rio de Janeiro", 6390290))
rj.adicionaCidade(Cidade("São Gonçalo", 1016128))
rj.adicionaCidade(Cidade("Duque de Caixias", 867067))


for estado in [am, sp, rj]:
    print(f"Estado: {estado.nome} Sigla: {estado.sigla}")
    for cidade in estado.cidades:
        print(f"Cidade: {cidade.nome} População: {cidade.populacao}")
    print(f"População do Estado: {estado.populacao()}\n")