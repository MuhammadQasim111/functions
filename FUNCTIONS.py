
def add(x, y): 
     return x + y

def subtract(x, y): 
     return x - y

def divide(x, y): 
    if y == 0: 
     return x / y # return "Error: Division by zero is undefined" return x / y

def multiply(x, y):
     return x * y

def calculator(): 
    while True: 
        print("\n1. Add") 
        print("2. Subtract") 
        print("3. Multiply") 
        print("4. Divide") 
        print("5. Exit")

    # Get user input for the operation
    option = input("Enter what you want: ")
    if option == '5':
        print("Exiting the calculator.")
        break   # if i dont perform break then  on entering 5, my program will not work

    # Check if the choice is valid
    if option in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue
# Perform the chosen operation
        if option == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif option == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif option == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif option == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid choice! Please choose a valid operation.")
#Run the calculator
if name == "main":
    calculator()   
    
    
    #%%
    
    
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is undefined"
    return x / y

def calculator():
    while True:
        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        option = input("Enter your choice: ")

        if option == '5':
            print("Exiting the calculator.")
            break

        if option not in ['1', '2', '3', '4']:
            print("Invalid choice! Please choose a valid operation.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if option == '1':
            result = add(num1, num2)
        elif option == '2':
            result = subtract(num1, num2)
        elif option == '3':
            result = multiply(num1, num2)
        elif option == '4':
            result = divide(num1, num2)

        print(f"Result: {result}")

if __name__ == "__main__":
    calculator()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    






