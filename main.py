import random

options = ('piedra', 'papel', 'tijera')

userOption = input('piedra, papel o tijera => ')
computerOption = random.choice(options)
userOption = userOption.lower()

if not userOption in options:
  print ('Esa opcion no es valida')

print(userOption)

print('User option =>', userOption)
print('Computer option =>', computerOption)

if userOption == computerOption:
  print('Empate!')
elif userOption == 'piedra':
  if computerOption == 'tijera':
    print ("Usuario Gana!")
  else:
    print ("Computadora Gana!")

elif userOption == 'papel':
  if computerOption == 'piedra':
    print ("Usuario Gana!")
  else:
    print ("Computadora Gana!")

elif userOption == 'tijera':
  if computerOption == 'papel':
    print ("Usuario Gana!")
  else:
    print ("Computadora Gana!")






  
  