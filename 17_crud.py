# CRUD, Create, Read, Update & Delete

numbers = [1, 2, 3, 4, 5]
print(numbers[1])
numbers[-1] = 10
print(numbers)

numbers.append(700)
print(numbers)

numbers.insert(0, "hola")
print(numbers)

numbers.insert(3, "change")
print(numbers)

tasks = ['todo 1', 'todo 2', 'todo 3']
newList = numbers + tasks
print(newList)

index = newList.index('todo 2')
newList[index] = 'todo changed'
print (newList)

newList.remove('todo 1')
print(newList)

newList.pop()
print(newList)
newList.pop(0)
print(newList)

newList.reverse()
print(newList)

numbersA = [1, 4, 6, 3]
numbersA.sort()
print(numbersA)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)



'''
append(): Añade un ítem al final de la lista.
clear(): Vacía todos los ítems de una lista.
extend(): Une una lista a otra.
count(): Cuenta el número de veces que aparece un ítem.
index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
insert(): Agrega un ítem a la lista en un índice específico.
pop(): Extrae un ítem de la lista y lo borra.
remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
reverse(): Le da la vuelta a la lista actual.
sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.
'''