from flask import Flask
from call import callMedianteJson 

app = Flask(__name__)

#Ruta indice "inicio"
@app.route('/')
def index():
    salida = "<h1>Pronostico del tiempo: San Francisco</h1></br><h2>Version 2</h2></br><a>Esta es la predicción del tiempo en San Francisco, esta predicción se ha realizado con Forecast</a></br></br><a href='http://127.0.0.1:5000/24horas'>Predicción día 1 (24 horas) </a></br><a href='http://127.0.0.1:5000/48horas'>Predicción día 2 (48 horas) </a></br><a href='http://127.0.0.1:5000/72horas'>Predicción día 3 (72 horas) </a>",200
    return salida

#Ruta llamada 24 horas
@app.route('/24horas')
def call24horas():
    salida = callMedianteJson(24)
    return salida.to_html(),200

#Ruta llamada 48 horas
@app.route('/48horas')
def call48horas():
    salida = callMedianteJson(48)
    return salida.to_html(),200

#Ruta llamada 72 horas
@app.route('/72horas')
def call72horas():
    salida = callMedianteJson(72)
    return salida.to_html(),200

if __name__ == '__main__':
    app.run(debug=True)
