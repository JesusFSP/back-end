from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Bienvenido a mi pagina web con flask</h1>'

@app.route('/saludo')
def saludo():
    nombre = request.args.get('nombre', 'no hay nombre')
    return '<center>Hola {}</center>'.format(nombre)

@app.route('/suma')
def suma():
    n1 = request.args.get('n1', '0')
    n2 = request.args.get('n2', '0')
    resultado = int(n1) + int(n2)
    return '<h1> la suma es {}</h1>'.format(resultado)

app.run(debug=True)   