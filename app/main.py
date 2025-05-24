from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def home():
    return "API funcionando en contenedor optimizado"
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)