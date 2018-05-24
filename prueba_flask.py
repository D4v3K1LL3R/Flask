from flask import Flask


app = Flask(__name__)

@app.route('/')
def hola():
    return 'hola mundo'

app.run(debug=True, port=8000, host='0.0.0.0')
