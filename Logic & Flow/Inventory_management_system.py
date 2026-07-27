inventory={}
def add_item(item,price,stock):
    if item in inventory:
        print(f"Error: Item '{item}' already exists.")
    else:
        inventory[item]={
            "price":float(price),
            "stock":int(stock)
        }
        print(f"Item '{item}' added successfully.")

add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
add_item("Apple", 0.6, 30)  # Should print an error
print(inventory)  