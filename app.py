from flask import Flask, render_template

app = Flask(__name__)

# Definimos las rutas de tu plataforma
@app.route('/')
def index():
    # Estas son las variables que mencionaste anteriormente. 
    # Si tu index.html pide alguna otra, simplemente agrégala aquí como: 'nombre': valor
    datos = {
        'total_e': 0,
        'total_enc': 0
    }
    return render_template('index.html', **datos)

@app.route('/entrevista')
def entrevista():
    return render_template('entrevista.html')

@app.route('/encuesta')
def encuesta():
    return render_template('encuesta.html')

@app.route('/resultados')
def resultados():
    return render_template('resultados.html')

@app.route('/exportar')
def exportar():
    return "Exportar en construcción"

# NOTA: No incluyas 'if __name__ == "__main__":' 
# porque Vercel lo gestiona automáticamente.
