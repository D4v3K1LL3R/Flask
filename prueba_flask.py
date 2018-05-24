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

#suma
@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):#creacion de una vista

    return '{}+{}={}'.format(num1,num2,num1+num2)

#suma.html
@app.route('/adds/<int:num1>/<int:num2>')
@app.route('/adds/<float:num1>/<float:num2>')
@app.route('/adds/<float:num1>/<int:num2>')
@app.route('/adds/<int:num1>/<float:num2>')
@app.route('/adds/<int:num1>/<int:num2>')
def adds(num1,num2):#creacion de una vista

    return render_template("add.html",num1=num1,num2=num2)

app.run(debug=True, port=8000, host='0.0.0.0')
