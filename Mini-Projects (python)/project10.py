#consetion stand Programme

menu = {"fried rice" : 780.00,
        "pizza": 2100.00,
        "spagattie" :1500.00,
        "noodles":1100.00,
        "chips":550.00,
        "soda": 250.00,
        "lemonade" :250.00}

cart = []
total = 0

print("--------MENU--------")
for key, value in menu.items() :
 print(f"{key:10} : ${value:.2f}")
print("--------------------")

while True:
  food = input("Select an item (q to quit): ").lower()
  if food == "q":
   break
  elif menu.get(food) is not None:
    cart.append(food)

print("--------Your Order--------")
for food in cart:
  total = total + menu.get(food)
  print(food, end = " ")

print()
print(f"Total is: ${total:.2f}")
