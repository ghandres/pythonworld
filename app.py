from flask import Flask,  request, make_response, abort, url_for, redirect, render_template
from jinja2 import Template

app = Flask(__name__)


@app.route('/')
def welcome():
    print(url_for('welcome'))
    return render_template('base.html', nombre="Andres")


@app.route('/hello/')
@app.route('/hello/<string:name>')
def hello(name=None):
    if name:
        return f'<h1>Hello World {name} </h1>'
    else:
        return '<h1>Hello Mundo Nada </h1>'


@app.route('/posteando/', methods=['POST', 'GET'])
def post():
    if request.method == 'GET':
        return "A la pantalla de inicio"
    else:
        return "Llega el formulario"


@app.errorhandler(404)
def error(error):
    print(error)
    return render_template("error.html", error=error)


if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)
