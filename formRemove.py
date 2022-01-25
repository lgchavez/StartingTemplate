from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class DeleteForm(FlaskForm):
  removeMessage=StringField('delete task')
  delete = SubmitField('delete')