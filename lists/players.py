# fatiando uma lista
players = ['maria', 'angelina', 'jose', 'antonio', 'elizandra', 'felipe']
print(players[1:3])
print(players[1:4])
print(players[:4])

print("Here are the firts three players on my team:")
for player in players[:3]:
    print(player.title())

# copiando uma lista
my_foods = ['hamburguer', 'pão na chapa', 'pizza', 'macarronada']
friends_food = my_foods[:]

print('My favorite foods are:')
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_food)

my_foods.append('cannoli')
friends_food.append('ice cream')

print('My favorite foods are:')
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_food)