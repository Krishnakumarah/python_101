seat=input("Enter yes/no do you want seat: ")
yes=True
no=False
seat = True
i=seat
while seat and i<=8:
    i=int(input("enter your seat no.: "))
    print(f"seat is booked: {i}")
    seat+=i
    print("enter the seat between 1 to 8")
else:
    print("seat is full ")      