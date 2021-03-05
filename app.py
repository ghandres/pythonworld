from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def welcome():
    print(url_for('welcome'))
    return '<h1>Welcome</h1>'


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


if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)
