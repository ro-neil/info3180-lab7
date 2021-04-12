from flask_wtf import FlaskForm
from wtforms importTextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class UploadForm(FlaskForm):
    description = TextAreaField('description', validators=[DataRequired()])
    photo = FileField('photo', validators=[
        FileRequired(),
        FileAllowed(['jpg','png','jpeg','svg'], 'Images only')
    ])