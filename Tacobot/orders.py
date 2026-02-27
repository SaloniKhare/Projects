
menu={
  "chicken tacos":10.0,
  "grilled pork tacos":12.0,
  "vegetarian tacos":8.0,
  "beef tacos":15.0,
  "coffee":3.0,
  "coke":5.0,
  "orange juice":4.0
}
total_price=0.0
def order():
  while True:
        user_input = input("You: ")
        global total_price
        if user_input.lower() == "done":
            print("TacoBot🌮: Thank you for your order! ")
            break

        if user_input not in menu:
            print("TacoBot🌮: I'm sorry, we don't have that item. Please choose from the menu.")
            continue

        try:
            print(f"TacoBot🌮: How many {user_input}(s) would you like?")
            quantity = int(input("You👨:Anything else?? "))
            if quantity <= 0:
                print("TacoBot🌮: Quantity must be at least 1.")
                continue
        except ValueError:
            print("TacoBot🌮: Please enter a valid quantity.")
            continue

        # Calculate total price
        total_price = total_price + (menu[user_input] * quantity)
  return total_price




