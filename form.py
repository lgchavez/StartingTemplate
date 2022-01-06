from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class MessageForm(FlaskForm):
    message = StringField('Add a task')
    submit = SubmitField('Add')