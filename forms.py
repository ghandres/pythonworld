from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, SubmitField, StringField
from wtforms.validators import InputRequired 


class form_usuario (FlaskForm):
    name = StringField ("Nombre", validators=[InputRequired('Nombre Obligatorio')])
    edad = IntegerField("Edad", validators=[InputRequired('introduce una edad')])
    submmit = SubmitField("Aceptar")
