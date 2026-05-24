from flask import Flask, render_template

app = Flask(__name__)  # Vercel busca específicamente esta variable 'app'

@app.route('/')
def index():
    # Aquí definimos un "diccionario" de seguridad con todas las variables que tu HTML pudiera estar pidiendo
    # Ponles 0 a todas para que la página cargue sí o sí.
    variables = {
        'total_e': 0,
        'total_enc': 0,
        'otra_variable': 0,
        'nombre_usuario': 'Invitado'
    }
    return render_template('index.html', **variables)

# ... (tus otras rutas aquí)

# QUITA O COMENTA la parte de 'if __name__ == "__main__":'
# A Vercel no le gusta eso cuando despliegas, le estorba.
# if __name__ == '__main__':
#     app.run()
