from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField

class MessageForm(FlaskForm):
    message = StringField('Add a task')
    submit = SubmitField('Add')
    flag = BooleanField ('important')
