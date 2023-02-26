from ecommerce_project.item_package.item_module import Item
from ecommerce_project.shopping_cart.shopping_cart_module import ShoppingCart

item1 = Item(description='Shirt Description')
item2 = Item(description='Pant Description')

print()
print(item1.display_description)
print(item2.display_description)

# item1 = item2
# print(item1.display_description) => Pant Description
# print(item2.display_description) => Pant Description

item1 = Item(1551,'Shirt Descriptio',10,450)
item2 = Item(1672,'Pant Description',5,700)

final_item1_price = item1.quantity * item1.price
final_item2_price = item2.quantity * item2.price

print('\nPrice for item2 : ', final_item1_price)
print('Final price for Item 1 after discount:', ShoppingCart.discount(item1.quantity, final_item1_price))

print('\nPrice for item 2: ', final_item2_price)
print('Final price for Item 2 after discount:', ShoppingCart.discount(item2.quantity, final_item2_price))
