from flask import Flask,  request, make_response, abort, url_for, redirect, render_template
from jinja2 import Template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def welcome():
    print(url_for('welcome'))
    return render_template('welcome.html', nombre="Andres")


@app.route('/hello/')
@app.route('/hello/<string:name>')
def hello(name=None):
    if name:
        return render_template("hello.html", nombre=name)
    else:
        return render_template("hello.html", nombre='Desconocido')


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
