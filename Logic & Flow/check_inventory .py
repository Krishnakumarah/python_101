def check_inventory(inventory, item):
    # Write code here
    if item in inventory:
        quantity = inventory[item]
        print(f"{item} is in stock. Quantity: {quantity}")
    else:
        print(f"{item} is not in stock.") 