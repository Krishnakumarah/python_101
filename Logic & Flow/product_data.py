def print_product_details(product_data):
    # Write code here
    if not product_data:
        print("No product information available")
    else:
        for key,value in product_data.items():
            print(f"{key.capitalize()}: {value}")

my_product={{"name":"Laptop","brand":"Dell","price":799.99,"stock":15}}
print_product_details(my_product)
            
print_product_details({})