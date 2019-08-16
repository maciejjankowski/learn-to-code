def is_it_adam(name):
  if name == 'Adam':
    return True
  else:
    return False

name = input("Pls gib name")

if is_it_adam(name):
  print('not you again...')
else:
  print("Hi!")

print(name)
