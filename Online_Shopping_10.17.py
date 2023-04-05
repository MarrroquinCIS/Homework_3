# luis Marroquin
# 1975448
# CIS-2348
# Online Shopping  10.17 Part-1

class ItemToPurchase:
    def __init__(self):
        # initialize the attributes
        self.item_name = None
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        # print the output in the format
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")


if __name__ == "__main__":
    print('Item 1')
    item1 = ItemToPurchase()
    item1.item_name = input('Enter the item name:\n')
    item1.item_price = int(input('Enter the item price:\n'))
    item1.item_quantity = int(input('Enter the item quantity:\n'))

    # for item 2
    print('\nItem 2')
    item2 = ItemToPurchase()
    item2.item_name = input('Enter the item name:\n')
    item2.item_price = int(input('Enter the item price:\n'))
    item2.item_quantity = int(input('Enter the item quantity:\n'))

    # print the costs
    print('\nTOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()

    # print the total cost
    print(f"\nTotal: ${item1.item_price * item1.item_quantity + item2.item_price * item2.item_quantity}")