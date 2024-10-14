print("Welcome to the Python Pizza Deliveries!!")
size = input("What size pizza do you want? S, M, or L: ").upper()  # Added ()
Pepperoni = input("Do you want pepperoni on your pizza? y or n: ").lower()  # Added ()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()  # Added ()
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Wrong entry for size.")
    exit()

if Pepperoni == "y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")
