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
            
        except Exception as e:def handle_shopping_cart(orders):
    # Create an empty dictionary for the shopping cart
    cart={}
    # Process each order in the list
    for order in orders:
        try:
            if ":" not in order:
                print(f"Invalid format: {order}")
                continue
            # Split the order and add to cart
            item=order.split(":")[0]
            quantity_str=order.split(":")[1]
            quantity=int(quantity_str)
            if quantity<0:
                print(f"Negative quantity not allowed: {order}")
                continue
            if item in cart:
                cart[item]+=quantity
            else:
                cart[item]=quantity
            # Handle potential errors
            
        except ValueError:
            # Handle value errors
            print(f"Invalid quantity: {order}")
        except Exception as e:
            # Handle unexpected errors
             print(f"Unexpected error: {e}")
    # Return the completed cart
    return cart
            # Handle unexpected errors
            
    # Return the completed cart