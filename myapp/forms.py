from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class RecipeForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Post')

    