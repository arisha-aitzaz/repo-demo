def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
operations= {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
num1= int(input("Enter first number: "))
for symbol in operations:
    print(symbol)

continue_flag= True
while continue_flag:
 op=input("Choose a symbol: ")
 num2= int(input("Enter second number: "))
 calculation= operations[op]
 result= calculation(num1, num2)
 print(f"{num1} {op} {num2} = {result}")

 choice= input(f"Enter 'y' to continue calculation with {result} or 'n' to exit.")
 if choice== "y":
    num1= result
 else:
    continue_flag= False
    print("Bye")