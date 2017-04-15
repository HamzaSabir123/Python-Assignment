#-----------Exercise 4.11-------------
myPizza=['Peporrani Pizza','Thin Crust Pizza','Thick Crust Pizza']
print('My favorite pizza : '+str(myPizza))

freindsPizza=myPizza[:]
print('My friends pizza : '+str(freindsPizza))
print('\n')

myPizza.append('Hawaiian Pizza')
freindsPizza.append('Veggie Pizza')

print('My favorite pizzza : '+str(myPizza))
print('My friends pizza : '+str(freindsPizza))
print('\n')


#-----------Exercise 4.12-------------
myPizzas=['Peporrani Pizza','Thin Crust Pizza','Thick Crust Pizza']
for myFavorite in myPizzas:
    print('My Favorite Pizzas are : '+ str(myFavorite))
print('\n')

freindsPizzas=myPizzas[:]
for freindsFavorite in freindsPizzas:
    print('My Freinds favorite Pizzas are : '+str(freindsFavorite))

myPizzas.append('Hawaiian Pizza')
freindsPizzas.append('Veggie Pizza')

for myFavorite in myPizzas:
    print('My Favorite Pizzas are : '+ str(myFavorite))
print('\n')

for freindsFavorite in freindsPizzas:
    print('My Freinds favorite Pizzas are : '+str(freindsFavorite))