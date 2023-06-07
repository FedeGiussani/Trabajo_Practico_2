from modules.cajonAlimento import CajonAlimento
from modules.cintaTransportadora import CintaTransportadora 

def main():
    cin_tr = CintaTransportadora() #creo una cinta

    N=int(input("Ingrese el número de alimentos: "))

    cin_tr.iniciar_transporte(N)

    lista_alimentos=cin_tr.getAlimentos() #lista de tuplas con (alimento, peso)

    cajon=CajonAlimento(lista_alimentos) #creo un cajon 


    aw_alimentos=cajon.aw_promedio() #diccionario que tiene toda las aw
    print(f"La actividad acuosa promedio de las manzanas es: {aw_alimentos['aw_manzanas']}")
    print(f"La actividad acuosa promedio de los kiwis es: {aw_alimentos['aw_kiwis']}")
    print(f"La actividad acuosa promedio de las zanahorias es: {aw_alimentos['aw_zanahorias']}")
    print(f"La actividad acuosa promedio de las papas es: {aw_alimentos['aw_papas']}")
    print(f"La actividad acuosa promedio de las frutas es: {aw_alimentos['aw_frutas']}")
    print(f"La actividad acuosa promedio de las verduras es: {aw_alimentos['aw_verduras']}")
    print(f"La actividad acuosa promedio total es: {aw_alimentos['aw_total']}")

    for clave, valor in aw_alimentos.items():
        if cajon.advertencia(valor):
            print(f"La {clave} se pasa de 0,95")

main ()
