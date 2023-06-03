from modules.cajon_alimentos import Cajon_alimentos
from modules.cintaTransportadora import CintaTransportadora 

cin_tr = CintaTransportadora() #creo una cinta

#N=int(input("Ingrese el número de alimentos: "))
N=10

CintaTransportadora.iniciar_transporte(cin_tr, N)
print(f"Alimentos y sus pesos: {cin_tr.getAlimentos()}")

lista_alimentos=cin_tr.getAlimentos() #lista de tuplas con (alimento, peso)

cajon=Cajon_alimentos(lista_alimentos) #creo un cajon 

cajon.org_alimentos() #clasifico los alimentos en frutas y verduras
cajon.org_frutas() #clasifico frutas
cajon.org_verduras() #clasifico verduras
aw_alimentos={
    "aw_prom_frutas":cajon.aw_prom_frutas(),
    "aw_prom_verduras":cajon.aw_prom_verduras(),
    "aw_prom_total":cajon.aw_total(),
    "aw_manzanas":cajon.aw_manzanas(),
    "aw_kiwis":cajon.aw_kiwis(),
    "aw_papas":cajon.aw_papas(),
    "aw_zanahorias":cajon.aw_zanahorias(),
}
"""aw_prom_frutas=cajon.aw_prom_frutas()
aw_prom_verduras=cajon.aw_prom_verduras()
aw_prom_total=cajon.aw_total()
aw_manzanas=cajon.aw_manzanas()
aw_kiwis=cajon.aw_kiwis()
aw_papas=cajon.aw_papas()
aw_zanahorias=cajon.aw_zanahorias()"""

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

"""
arreglo_alimentos = CintaTransportadora.getAlimentos(cin_tr)

Alimento.org_alimentos(al, arreglo_alimentos)

Fruta.org_frutas(fr, al.getFrutas())
Verdura.org_verduras(verd, al.getverduras())


print(al.getFrutas())
print(al.getverduras())

#print(fr.getManzana())
#print(fr.getKiwi())
#print(verd.getZanahoria())
#print(verd.getPapas())


aw_k = 0
for ki in fr.getKiwi():
    aw_k += Kiwi.aw_kiwi(k, ki)


if len(fr.getKiwi()) > 0:
    aw_k = aw_k/len(fr.getKiwi())

   
print("La actividad acuosa promedio del kiwi es: ")
print(al.redondear(aw_k)) 

aw_m = 0
for man in fr.getManzana():
    aw_m += Manzana.aw_manzana(m, man)

if len(fr.getManzana()) > 0:    
    aw_m = aw_m/len(fr.getManzana())
    
print("La actividad acuosa promedio de la manzana es: ")
print(al.redondear(aw_m) ) 
    
aw_p = 0
for pa in verd.getPapas():
    aw_p += Papa.aw_papa(p, pa)

if len(verd.getPapas()) > 0:
    aw_p = aw_p/len(verd.getPapas())

print("La actividad acuosa promedio de la papa es: ")
print( al.redondear(aw_p) )
 
aw_z = 0
for zan in verd.getZanahorias():
    aw_z += Zanahoria.aw_zanahoria(z, zan)
    
if len(verd.getZanahorias()) > 0:    
    aw_z = aw_z/len(verd.getZanahorias())
    
print("La actividad acuosa promedio de la zanahoria es: ")
print( al.redondear(aw_z) ) 

prom_frutas = Fruta.aw_prom_frutas(fr, aw_k, aw_m) 
print("La actividad acuosa promedio de las frutas es: " )
print(al.redondear(prom_frutas))
prom_verduras = Verdura.aw_prom_verduras(verd, aw_z, aw_p) 
print("La actividad acuosa promedio de las verduras es: " )
print(al.redondear(prom_verduras))


prom_total = Alimento.aw_total(al, prom_frutas, prom_verduras)
print("La actividad acuosa promedio total del conjunto de alimentos es: ")
print(al.redondear(prom_total))

Alimento.advertencia(al, aw_k,"kiwi")
Alimento.advertencia(al, aw_m,"manzana")
Alimento.advertencia(al, aw_p,"papa")
Alimento.advertencia(al, aw_z,"zanahoria")
Alimento.advertencia(al, prom_frutas,"frutas")
Alimento.advertencia(al, prom_verduras,"verduras")
Alimento.advertencia(al, prom_total,"conjunto alimentos")
"""
