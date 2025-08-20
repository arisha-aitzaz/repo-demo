menu = {
    'Pizza': 40,
    'Burger': 50,
    'Coffee': 80,
    'Pasta': 60,
    'Salad': 70,
}
print("Welcome, here is the menu: ")
print("Pizza: Rs.40\nBurger: Rs.50\nCoffee: Rs.80\nPasta: Rs.60\nSalad: Rs.70")
total_bill = 0
first_item = input("Enter the first item you want to order: ")
if first_item in menu: 
  print("Item added to cart.")
  total_bill= total_bill + menu[first_item]
else:
  print("Item not available")
another_item = input("Do you want to order another item? ")
if another_item == "Yes":
  item_2= input("Enter second item: ")
  if item_2 in menu:
    print("Item added to cart.")
    total_bill= total_bill + menu[item_2]
    print("Total bill is", total_bill)
  else:
    print("Item not available")
else:
  print("Total bill is", total_bill)
print("Thank you for your order!")

   