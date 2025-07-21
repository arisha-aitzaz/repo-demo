#Define the menu of restaurant
menu= {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Coffee': 80,
}
print("Welcome to the Restaurant. Here's the menu:")
print("pizza: Rs 40\npasta: Rs 50\nburger: Rs 50\ncoffee: Rs 80")
total_bill= 0
item_1= input("Enter the first item you want to buy:")
if item_1 in menu:
    total_bill += menu [item_1]
    print(f"Your item {item_1} has been added to your order.")
else: 
    print(f"Selected item is not in the menu.")
    
item_2= input("Do you want to order something else?")
if item_2== "Yes":
        item_2= input("Please enter the name of the second item:")
        if item_2 in menu: 
            total_bill += menu [item_2]
            print("Your total bill is", total_bill)
        else:
             print("Selected item is not in the menu.")
else: 
     print("Thankyou for your order. Your total bill is", total_bill)