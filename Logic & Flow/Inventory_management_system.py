inventory={}
  # Should output: {}
def add_item(item, price, stock):
    if item in inventory:
        print(f"Error: Item '{item}' already exists.")
    else:
        inventory[item]={
            "price":float(price),
            "stock":int(stock)
        }
        print(f"Item '{item}' added successfully.")
def update_stock(item,quantity):
    if item not in inventory:
        print(f"Error: Item '{item}' not found.")
        return
    
    new_stock = inventory[item]["stock"] + quantity
    if new_stock < 0:
        print(f"Error: Insufficient stock for '{item}'.")
        return
        
    # FIX: Update ONLY the "stock" key inside the nested dictionary
    inventory[item]["stock"] = new_stock
    print(f"Stock for '{item}' updated successfully.")
def check_availability(item):
    if item not in inventory:
        return "Item not found"
    return inventory[item]["stock"]
add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
update_stock("Apple", -20)
update_stock("Banana", 30)
print(check_availability("Apple"))  # Should return 80
print(check_availability("Banana"))  # Should return 80
print(check_availability("Orange"))  # Should return "Item not found"
 

