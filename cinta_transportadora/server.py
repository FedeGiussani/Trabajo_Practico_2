from flask import Flask, app, render_template, request
from modules.cintaTransportadora import CintaTransportadora
from modules.alimento import Alimento
from modules.fruta import Fruta 
from modules.verdura import Verdura 
from modules.kiwi import Kiwi 
from modules.manzana import Manzana 
from modules.papa import Papa 
from modules.zanahoria import Zanahoria 

app = Flask(__name__)

N=0

@app.route("/", methods=['GET', 'POST'])
def raiz():
    global N    

    if request.method == 'POST':
       N= int(request.form.get("N"))

    return render_template("home.html") 

@app.route("/cinta", methods=['GET', 'POST'])
def cinta():
    global N
    
    al = Alimento()
    cin_tr = CintaTransportadora()   
    fr = Fruta()
    verd = Verdura()
    k = Kiwi()
    m = Manzana()
    p= Papa()
    z = Zanahoria()

    CintaTransportadora.iniciar_transporte(cin_tr, N)  

    arreglo_alimentos = CintaTransportadora.getAlimentos(cin_tr)

    Alimento.org_alimentos(al, arreglo_alimentos)

    Fruta.org_frutas(fr, al.getFrutas())
    Verdura.org_verduras(verd, al.getverduras())
    
    aw_k = 0
    for ki in fr.getKiwi():
        aw_k += Kiwi.aw_kiwi(k, ki)
    if len(fr.getKiwi()) > 0:
        aw_k = aw_k/len(fr.getKiwi())

    aw_k=al.redondear(aw_k)

    aw_m = 0
    for man in fr.getManzana():
        aw_m += Manzana.aw_manzana(m, man)

    if len(fr.getManzana()) > 0:    
        aw_m = aw_m/len(fr.getManzana())
    
    aw_m=al.redondear(aw_m)
        
    aw_p = 0
    for pa in verd.getPapas():
        aw_p += Papa.aw_papa(p, pa)

    if len(verd.getPapas()) > 0:
        aw_p = aw_p/len(verd.getPapas())

    aw_p=al.redondear(aw_p)
    
    aw_z = 0
    for zan in verd.getZanahorias():
        aw_z += Zanahoria.aw_zanahoria(z, zan)
        
    if len(verd.getZanahorias()) > 0:    
        aw_z = aw_z/len(verd.getZanahorias())
        
    aw_z=al.redondear(aw_z) 

    prom_frutas = Fruta.aw_prom_frutas(fr, aw_k, aw_m) 
    prom_frutas=al.redondear(prom_frutas)
    prom_verduras = Verdura.aw_prom_verduras(verd, aw_z, aw_p)
    prom_verduras=al.redondear(prom_verduras)


    prom_total = Alimento.aw_total(al, prom_frutas, prom_verduras)
    prom_total=al.redondear(prom_total)

    advertencia=[]
    advertencia.append(Alimento.advertencia_web(al, aw_k,"kiwi"))
    advertencia.append(Alimento.advertencia_web(al, aw_m,"manzana"))
    advertencia.append(Alimento.advertencia_web(al, aw_p,"papa"))
    advertencia.append(Alimento.advertencia_web(al, aw_z,"zanahoria"))

    return render_template("cinta.html", aw_k=aw_k, aw_m=aw_m, aw_p=aw_p, aw_z=aw_z, prom_frutas=prom_frutas, prom_verduras=prom_verduras, prom_total=prom_total, advertencia=advertencia)

if __name__ == "__main__":
    app.run(debug=True)