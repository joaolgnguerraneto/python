motorcycles = ["honda", "ducati", "yamaha", "suzuki", "bmw"]
print(motorcycles)

# modificando elementos de uma lista
motorcycles[0] = "kavasaki"
print(motorcycles)

# concatnando elementos no final de uma lista  o método "append()" para adicionar elemento no final da lista
motorcycles.append('harley davidson')
print(motorcycles)

model_motorcycles = []
model_motorcycles.append('150 c')
model_motorcycles.append('250 c')
model_motorcycles.append('300 c')
model_motorcycles.append('500 c')
model_motorcycles.append('800 c')
model_motorcycles.append('1200 c')
model_motorcycles.append('another')
print(model_motorcycles)

# acrescentando elementos na lista usando o método "insert()"
motorcycles.insert(6, 'mobilete')
print(motorcycles)

# deletando elementos na lista usando o método "del"
del motorcycles[6]
print(motorcycles)

# removendo um iem com o elemento "pop()"
popped_motocycle = motorcycles.pop()
print(motorcycles)
print(popped_motocycle)

# método "remove()" para remover
too_expensive   = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

# ordenando uma lista de forma permanente com o método "sort()"
cars = ["peugout", "volkswagem", "fiat", "bmw", "ferrari", "toyota", "mitisubishi", "saburu", "ford"]
cars.sort()
print(cars)

# invert
cars.sort(reverse=True)
print(cars)

# ordenando temporariamente
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))


# lista em ordem cronológica
cars.reverse()
print(cars)

print(len(cars))