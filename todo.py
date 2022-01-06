todo=[]
if len(todo)>0:
  print("what would you like to remove")
  remove = input()
  todo.remove(remove)
  print(todo)
if len(todo)==0:
  print("what do you like to do after school")
  remove = input()
  todo.append(remove)
if len(todo)>0:
  print("what is your favorite sport")
  remove = input()
  todo.append(remove)