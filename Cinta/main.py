from modules.alimento import alimento 
from modules.cinta_transportadora import cinta_transportadora 
from modules.frutas import frutas 
from modules.verduras import verduras 
from modules.kiwi import kiwi 
from modules.manzana import manzana 
from modules.papa import papa 
from modules.zanahoria import zanahoria 

al = alimento()
cin_tr = cinta_transportadora()   
fr = frutas()
verd = verduras()
k = kiwi()
m = manzana()
p= papa()
z = zanahoria()


N = 100

cinta_transportadora.iniciar_transporte(cin_tr,   N)  

arreglo_alimentos = cinta_transportadora.getAlimentos(cin_tr)

alimento.org_alimentos(al, arreglo_alimentos)

frutas.org_frutas(fr, al.getFrutas())
verduras.org_verduras(verd, al.getverduras())


print(al.getFrutas())
print(al.getverduras())

#print(fr.getManzana())
#print(fr.getKiwi())
#print(verd.getZanahoria())
#print(verd.getPapas())


aw_k = 0
for ki in fr.getKiwi():
    aw_k += kiwi.aw_kiwi(k, ki)


if len(fr.getKiwi()) > 0:
    aw_k = aw_k/len(fr.getKiwi())
    
print("La actividad acuosa promedio del kiwi es: ")
print( aw_k ) 

aw_m = 0
for man in fr.getManzana():
    aw_m += manzana.aw_manzana(m, man)

if len(fr.getManzana()) > 0:    
    aw_m = aw_m/len(fr.getManzana())
    
print("La actividad acuosa promedio de la manzana es: ")
print( aw_m ) 
    
aw_p = 0
for pa in verd.getPapas():
    aw_p += papa.aw_papa(p, pa)

if len(verd.getPapas()) > 0:
    aw_p = aw_p/len(verd.getPapas())

print("La actividad acuosa promedio de la papa es: ")
print( aw_p )
 
aw_z = 0
for zan in verd.getZanahoria():
    aw_z += zanahoria.aw_zanahoria(z, zan)
    
if len(verd.getZanahoria()) > 0:    
    aw_z = aw_z/len(verd.getZanahoria())
    
print("La actividad acuosa promedio de la zanahoria es: ")
print( aw_z ) 

prom_frutas = frutas.aw_prom_frutas(fr, aw_k, aw_m) 
print("La actividad acuosa promedio de las frutas es: " )
print(prom_frutas)
prom_verduras = verduras.aw_prom_verduras(verd, aw_z, aw_p) 
print("La actividad acuosa promedio de las verduras es: " )
print(prom_verduras)


prom_total = alimento.aw_total(al, prom_frutas, prom_verduras)
print("La actividad acuosa promedio total del conjunto de alimentos es: ")
print(prom_total)

alimento.advertencia(al, aw_k,"kiwi")
alimento.advertencia(al, aw_m,"manzana")
alimento.advertencia(al, aw_p,"papa")
alimento.advertencia(al, aw_z,"zanahoria")


