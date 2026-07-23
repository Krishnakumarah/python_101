def handle_shopping_cart(orders):
    # Create an empty dictionary for the shopping cart
    card={}
    # Process each order in the list
    for order in orders:
        try:
            if ":" not in order:
                print(f"Invalid format: {order}")
                continue
            # Split the order and add to cart
            item=order.split(":")[1]
            
            # Handle potential errors
            
        except ValueError:
            # Handle value errors
            
        except Exception as e:
            # Handle unexpected errors
            
    # Return the completed cart