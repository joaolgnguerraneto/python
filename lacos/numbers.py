# laco usando o método range()
for value in range(1,6):
    print(value)

# usando range() para criar uma lista de números
numbers = list(range(1,6))
print(numbers)

# ignorar números na lista por exemplo listar os números pares entre 1 e 10
# começa com o valor 2 que é somado a este valor 2. o valor 2 é somado remetidamente ate o valor final 11
even_numbers = list(range(2,11,2))
print(even_numbers)

# dez primeiros quadrados perfeitos (**) dois asteriscos representão exponenciais
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

# comprehension
squares = [value**2 for value in range(1,11)]
print(squares)
