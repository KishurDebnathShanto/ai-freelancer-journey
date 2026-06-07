# calculator.py — Day 2 Project
# Author: Kishur Debnath Shanto

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def main():
    print("🧮 Simple Calculator")
    print("1. Add  2. Subtract  3. Multiply  4. Divide")
    
    choice = input("Enter choice (1-4): ")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")
        return

    if choice == '1':
        print(f"Result: {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {divide(num1, num2)}")
    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()