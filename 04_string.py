name = "Andres"
lastName = "Rocha"
age = 22
print (name)
print (lastName)

fullName = name + " " + lastName
print (fullName)

quote = "I'm Andres"
print (quote)

quote2= 'She said "Hello"'
print (quote2)

#format

template = "Hola, mi nombre es " + name + " y mi apellido es " + lastName
print ('v1', template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, lastName)

print ('v2', template)

template = f"Hola, mi nombre es {name} y mi apellido es {lastName}"

print ('v3', template)

template = f"Hola, mi nombre es {name} y mi apellido es {lastName}, y mi edad es {age} years old"

print ('v4', template)