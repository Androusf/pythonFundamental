person = {
  'name': 'Andres',
  'lastName': 'Rocha',
  'langs' : ['python','java'],
  'age': 99
}

print(person)

person['name'] = 'Juan'
person['age'] -= 50
person['langs'].append('rust')
print(person)

del person ['lastName']
person.pop('age')
print(person)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())


