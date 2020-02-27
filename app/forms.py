from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, FloatField
from wtforms.validators import ValidationError, DataRequired, Length


class PostForm(FlaskForm):
    # select_tag = SelectField('Primary Tag', choices=[('embassy, social_facility')])
    select_tag = SelectField('Primary Tag', choices=[
        ('all', 'All'), ('embassy', 'Embassy'), ('social_facility', 'Social Facility')])
    submit_filter = SubmitField('Filter')
