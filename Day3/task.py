#Check if the number is odd or even

# number = int(input("Give me any number: "))

# if number % 2 == 0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
total = 0

if size == "S":
    total = 15
elif size == "M":
    total = 20
elif size == "L":
    total = 25
else:
    print("You typed the wrong input, please use S, M or L")

if pepperoni == "Y":
    if size == "S":
        total += 2
    else:
        total += 3

if extra_cheese == "Y":
    total += 1

print(f"Your final bill is: ${total}")
