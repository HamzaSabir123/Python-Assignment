# Exercise 3.1

friend_list=['Hamza','Usman','Abul']
print(friend_list[0])
print(friend_list[1])
print(friend_list[2])

# Exercise 3.2

print('\nMyself Muhammad '+friend_list[0]+ ' Sabir')
print(friend_list[1]+' is my friend, classmate and group member of FYP as well.')
print(friend_list[2]+' is my friend, classmate and group member of FYP as well.\n')

# Exercise 3.3

vehicle_list=['Bick','Car','Bicycle']
print("I would like to own "+vehicle_list[1])
print("I don't like to own "+vehicle_list[2])

# Exercise 3.4

guest_list=['Ahmed','Shahab','Umair']
print('\nTo '+guest_list[0]+',I would like to invite you for dinner on 23rd of March.')
print('To '+guest_list[1]+',I would like to invite you for dinner on 23rd of March.')
print('To '+guest_list[2]+',I would like to invite you for dinner on 23rd of March.')

# Exercise 3.5


guest_list=['Ahmed','Shahab','Umair']
guest=guest_list.pop()
print('\n'+guest+" can't make dinner.\n")

# Modifying list of Array

print(guest_list)
guest_list.append('Shafique')
print(guest_list)

#--------OR----------

guest_list.insert(2,'Wahab')
print(guest_list)
print("To "+guest_list[2]+",I would like to invite you for dinner on 23rd of March.")