from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email

class BookForm(FlaskForm):
    title = StringField('Tytuł')
    autor = StringField('Autor')
    pages = IntegerField('Ilość stron')
    cover = BooleanField('Okładka')
    description = TextAreaField('Opis')
