from modules.cajonAlimento import CajonAlimento
from modules.cintaTransportadora import CintaTransportadora 

cin_tr = CintaTransportadora() #creo una cinta

N=int(input("Ingrese el número de alimentos: "))


cin_tr.iniciar_transporte(N)
#print(f"Alimentos y sus pesos: {cin_tr.getAlimentos()}")

lista_alimentos=cin_tr.getAlimentos() #lista de tuplas con (alimento, peso)

cajon=CajonAlimento(lista_alimentos) #creo un cajon 

aw_alimentos={
    "aw_prom_frutas":cajon.aw_prom_frutas(),
    "aw_prom_verduras":cajon.aw_prom_verduras(),
    "aw_prom_total":cajon.aw_total(),
    "aw_manzanas":cajon.aw_manzanas(),
    "aw_kiwis":cajon.aw_kiwis(),
    "aw_papas":cajon.aw_papas(),
    "aw_zanahorias":cajon.aw_zanahorias(),
}

print(f"La actividad acuosa promedio de las manzanas es: {aw_alimentos['aw_manzanas']}")
print(f"La actividad acuosa promedio de los kiwis es: {aw_alimentos['aw_kiwis']}")
print(f"La actividad acuosa promedio de las zanahorias es: {aw_alimentos['aw_zanahorias']}")
print(f"La actividad acuosa promedio de las papas es: {aw_alimentos['aw_papas']}")
print(f"La actividad acuosa promedio de las frutas es: {aw_alimentos['aw_prom_frutas']}")
print(f"La actividad acuosa promedio de las verduras es: {aw_alimentos['aw_prom_verduras']}")
print(f"La actividad acuosa promedio total es: {aw_alimentos['aw_prom_total']}")

for clave, valor in aw_alimentos.items():
    if cajon.advertencia(valor):
        print(f"La {clave} se pasa de 0,95")


