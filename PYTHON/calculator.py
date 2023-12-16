from colorama import Fore
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

def calculator():
    print("Simple Calculator")

    while True:
        try:
            num1 = float(input(Fore.BLACK+"Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        print(Fore.RED+ "\nSelect operation:")
        print(Fore.GREEN+"1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")

        try:
            choice = int(input(Fore.BLUE+"Enter your choice (1/2/3/4/5): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            result = add(num1, num2)
            print(Fore.CYAN+f"{num1} + {num2} = {result}")
        elif choice == 2:
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == 3:
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == 4:
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        elif choice == 5:
            print("Quitting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    calculator()
