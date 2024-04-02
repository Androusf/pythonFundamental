
'''
for element in range(1, 21):
  print (element)
'''

myList = [23, 45, 67, 89, 43]

for element in myList:
  print (element)

myTuple = ('nico', 'juli', 'santi')

for element in myTuple:
  print (element)

person = {
  'name': 'Andres',
  'lastName': 'Rocha',
  'age': 99
}

for element in person:
  print (element, '=>', person[element])

for element, value in person.items():
  print (element, '=>', value)

people = [
  {
    'name': 'andres',
    'age': 99
  },
  {
    'name': 'pepe',
    'age': 55
  },
  {
    'name': 'felipe',
    'age': 22
  }
]

for person in people:
  print ('name=>',person['name'])