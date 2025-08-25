
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/programacao')
def programacao():
    return render_template('programacao.html')

@app.route('/palestrantes')
def palestrantes():
    return render_template('palestrantes.html')

@app.route('/local')
def local():
    return render_template('local.html')

@app.route('/inscricoes')
def inscricoes():
    return render_template('inscricoes.html')

@app.route('/patrocinadores')
def patrocinadores():
    return render_template('patrocinadores.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)
