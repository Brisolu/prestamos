from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def index():
    # Esta es la pantalla principal que verán en el celular
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    datos = request.json
    monto = float(datos['monto'])
    tasa_anual = float(datos['tasa'])
    meses = int(datos['meses'])

    tasa_mensual = (tasa_anual / 100) / 12
    # Fórmula de cuota fija
    cuota = monto * (tasa_mensual / (1 - (1 + tasa_mensual)**-meses))
    
    return jsonify({
        "cuota": round(cuota, 2),
        "total": round(cuota * meses, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)
