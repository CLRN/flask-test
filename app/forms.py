from wtforms import Form, StringField
from wtforms.validators import DataRequired
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from flask_appbuilder.forms import DynamicForm
from flask_appbuilder import SimpleFormView
from flask_babel import lazy_gettext as _
from app import appbuilder


class MyForm(DynamicForm):
    field1 = StringField(('Field1'),
                         description=('Your field number one!'),
                         validators=[DataRequired()], widget=BS3TextFieldWidget())
    field2 = StringField(('Field2'),
                         description=('Your field number two!'), widget=BS3TextFieldWidget())
