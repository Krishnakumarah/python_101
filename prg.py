import random 
ans=random.randint(1,10)
guess_count=0
while True:
    guess =int(input("geuss a no. between 1 to 10:"))
    guess_count +=1
    if guess==ans:
        print("you guesse {guess_count} it in tries!")
        break
    elif guess<ans:
        print("too low.")
    else:
        print("too high.")