pin="1234"
attempt=0
while  attempt<=3:
    input_pin=input(f"Attempt={attempt} enter the correct pin:  ") 
    attempt+=1
    if input_pin==pin:
        print("correct")
        break

    else:
        print("incorrect")