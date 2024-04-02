myDict = {}
print (type(myDict))

myDict = {
  'avion': 'Fly',
  'name': 'Andres',
  'lastName': 'Rocha',
  'age': 30
}

print (myDict)
print (len(myDict))

print (myDict['age'])
print (myDict['lastName'])
print (myDict.get('age'))

print ('avion' in myDict)
print ('otroqueno' in myDict)