from flask import Flask, app, render_template, request
from modules.cintaTransportadora import CintaTransportadora
from modules.cajonAlimento import CajonAlimento

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
    
    cin_tr = CintaTransportadora() #creo una cinta

    CintaTransportadora.iniciar_transporte(cin_tr, N)

    lista_alimentos=cin_tr.getAlimentos() #lista de tuplas con (alimento, peso)

    cajon=CajonAlimento(lista_alimentos) #creo un cajon 
    aw_alimentos=cajon.aw_promedio()
    
    advertencia=[]
    for clave, valor in aw_alimentos.items():
        if cajon.advertencia(valor):
            aux= clave
            advertencia.append(aux)

    return render_template("cinta.html", aw_alimentos=aw_alimentos, advertencia=advertencia)

if __name__ == "__main__":
    app.run(debug=True)