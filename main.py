from flask import Flask, render_template, redirect
from form import MessageForm
from config import Config

app = Flask(
  'app',
  template_folder='templates'
)
app.config.from_object(Config)

my_message = []
def setMessage(message):
  global my_message
  my_message.append(message)
  print(my_message)

def deleteMessage(message):
  global my_message
  print(message)
  my_message.remove(message)
  print(my_message)

@app.route('/', methods=['GET', 'POST'])
def page_one():
  form = MessageForm()
  if form.is_submitted():
    print("made it")
    setMessage(form.data)
    return redirect('/display')
  return render_template('pageOne.html', form=form)

@app.route('/display', methods=['GET', 'POST'])
def page_two():
  deleteForm = MessageForm()
  print('pageTwo')
  if deleteForm.is_submitted():
    print("about to delete")
    deleteMessage(deleteForm.data.removeMessage)
    return redirect('/display')
  return render_template('pageTwo.html', my_message=my_message, deleteForm=deleteForm)

app.run(host='0.0.0.0', port=8080)
