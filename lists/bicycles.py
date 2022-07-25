bicycles = ['trek', 'connondale', 'redline', 'specialized']
print(bicycles)

bicycles = ['trek', 'connondale', 'redline', 'specialized']
print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[2].title())

# exibe o último elemento da lista
print(bicycles[-1].title())

# devolve o segundo item a partir do final da lista
print(bicycles[-2].title())

# exibe o terceiro item a partir do final da lista e assim sucessivamente
print(bicycles[-3].title())


message = ("My firts bicycle was a ") + bicycles[2].title() + "."
print(message)
