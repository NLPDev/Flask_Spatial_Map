from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, FloatField
from wtforms.validators import ValidationError, DataRequired, Length


class PostForm(FlaskForm):
    post = StringField('Spatial Data', validators=[DataRequired()])
    submit = SubmitField('Search')
