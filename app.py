from flask import Flask, render_template

app = Flask(__name__)  # Vercel busca específicamente esta variable 'app'

@app.route('/')
def index():
    # Si tu HTML dice {{ variable }}, aquí tienes que definirla:
    return render_template('index.html', 
        total_e=0, 
        total_enc=0,
        otra_variable_que_te_marque_error=0
    )

# ... (tus otras rutas aquí)

# QUITA O COMENTA la parte de 'if __name__ == "__main__":'
# A Vercel no le gusta eso cuando despliegas, le estorba.
# if __name__ == '__main__':
#     app.run()
