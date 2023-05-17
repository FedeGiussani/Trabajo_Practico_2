from flask import Flask, app, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def raiz():
          
    return render_template("home.html") 


if __name__ == "__main__":
    app.run(debug=True)