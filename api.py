from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/entrevista')
def entrevista():
    return render_template('entrevista.html')

@app.route('/encuesta')
def encuesta():
    return render_template('encuesta.html')

@app.route('/resultados')
def resultados():
    return render_template('resultados.html')
