name = input("Pls gib name")

def is_it_adam(name):
  if name == 'Adam':
    return True
  else:
    return False

if is_it_adam(name):
  print('not you again...')
else:
  print("Hi! " + name)
