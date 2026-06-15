# Restaurant menu
L = []
for i in range(1,6):
    item = input('enter the food name')
    price = int(input('enter the food price'))
    item_length = len(item)
    price_length = len(str(price))
    menu_item = item + ('-'*(20-item_length-price_length)) + str(price)
    L.append(menu_item)

print('Food Menu')
for x in L:
    print(x)



# Food Menu
# evwrgv------------45
# sdfvdbe-----------56
# dffsvsdv4---------45
# dfvdbvdbg---------56
# dvdgbdf34----------5