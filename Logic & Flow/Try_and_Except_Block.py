try:
    # Prompt the user to enter a number
    user_input = input()
    
    # Attempt to convert the input to a valid integer
    number = int(user_input)
    
    # Print the success message if no exception occurs
    print(f"You entered: {number}")

except ValueError:
    # Catch the exception if the input is not a valid integer
    print("Invalid input! Please enter a valid number.")