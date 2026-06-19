def login(email, password):

    correct_email = "user@example.com"
    correct_password = "SecretPassword123"
    
    
    if email == correct_email and password == correct_password:
        return "Login successful!"
    else:
        return "Invalid email or password."

status = login("user@example.com", "SecretPassword123")
print(status)