def process_data(input_string):
    try:
        # Try to convert the input string to an integer
        number=int(input_string)
        # Calculate 100 divided by the input value
        result=100/number
        # Return the result
        print(result)
    except ValueError:
        print ("Input must be a number!")
        # Handle the case where input cannot be converted to an integer
        
    except ZeroDivisionError:
        print ("Cannot divide by zero!")
        # Handle the case where input is zero
        
    except:
        # Handle any other unexpected exceptions
        print ("An unexpected error occurred!")
    return None