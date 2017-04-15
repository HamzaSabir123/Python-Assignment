#-----------Exercise 4.13-------------

# Restaurant's Menu
menues=('Sea Food','Chinese','Italian','Thi Food','Mexican Food')
for menu in menues:
    print('Restaurant Menu is : '+ str(menu))


# Update by making new tuple
menues=('Sea Food','Singaporian Food','Panama Food','Chinese','Italian')
for menu in menues:
    print('Restaurant has updated Menu : '+str(menu))



# Update menu directly
menues[2]='Singaporian Food'
for menu in menues:
    print('Restaurant Menu is : '+ str(menu))