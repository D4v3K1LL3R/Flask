from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name><ape>')
def index(name='Mundo', ape='Martinez'):#creacion de una vista
    name=request.args.get('name', name)
    ape=request.args.get('ape', ape)

    return 'Hola {}''{}'.format(name, ape)

app.run(debug=True, port=8000, host='0.0.0.0')
