from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length,Required
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from werkzeug.utils import secure_filename
# Set your classes here.
from wtforms import TextField, StringField,SelectField


class ProcessDataForm(Form):
    file = FileField('File', validators=[
        FileRequired(),
        FileAllowed(['xlsx', 'csv'], 'Excel only!')
    ])
    myChoices = [("", "select"), ('1', '1'), ('2', '2'), ('3', '3')]
    myChoices2 = [("", "select"),('5', '5'), ('6', '6'), ('7', '7')]
    first_choice = SelectField(u'List Categorical', choices=myChoices, validators=[DataRequired()])
    second_choice = SelectField(
        'list Numeric', choices=myChoices2, validators=[DataRequired()]
    )


