from flask import Flask, app, render_template
from modules.cintaTransportadora import CintaTransportadora 

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def raiz():
    


    #if request.method == 'POST':
     #   N= int(request.form.get("N"))

        
    return render_template("home.html") 


if __name__ == "__main__":
    app.run(debug=True)