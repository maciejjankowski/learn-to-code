help()
range()
len()
sorted()

dir()

import pprint
pprint.pprint(dir())

lista_rzeczy = list()
rzeczy_dziecka = []

rzeczy_dziecka.append("cukierek")
rzeczy_dziecka.append("zabawka")

rzeczy_dziecka.count()

rzeczy_dziecka.remove("cukierek")
rzeczy_dziecka.count()

rzeczy_dziecka.clear()

dziecko = {
  'wiek': 3.5,
  'rzeczy' : rzeczy_dziecka,
  'szczepienia' : ['koklusz']
}

dziecko.keys()
dziecko.values()

dziecko.clear()
pprint.pprint(dziecko)


"""
A function looks like this: function(something)
And a method looks like this: something.method()
(Look at the examples above!)

So why do we have both methods and functions in Python? 
The official answer is that there is a small difference between them. 
Namely: a method always belongs to an object 
(e.g. in the dog.append(4) method .append() needed the dog object 
to be applicable), while a function doesn’t necessarily. 
"""

# all python syntax in one place: 
# https://learnxinyminutes.com/docs/python3/

# All python built-in functions: 
# https://docs.python.org/3/library/functions.html

# Python language reference (all the things)
# https://docs.python.org/3/reference/index.html

# Python standard library (functions, data structures, modules, etc.)
# https://docs.python.org/3/library/index.html#library-index

