from flask import Flask, render_template

app = Flask(__name__)

# Esta función ayudará a que no falle si falta una variable en el HTML
@app.context_processor
def inject_defaults():
    return dict(total_e=0, total_enc=0, nombre_usuario='Invitado')

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
