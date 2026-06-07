# 📚 DAY 2 COMPLETE KNOWLEDGE COMPENDIUM
*Python Loops, Functions, Error Handling & First API Call | Teacher-Style Revision Guide*

---

## 🎯 WHAT YOU LEARNED TODAY (OBJECTIVES)
- ✅ Learned core Python control flow: `for`/`while` loops, functions (`def`), and error handling (`try`/`except`)
- ✅ Built a functional, error-proof CLI calculator (`calculator.py`)
- ✅ Configured and used Postman to make your first HTTP `GET` request
- ✅ Understood JSON structure and how software communicates over the internet
- ✅ Committed and pushed Day 2 progress to your GitHub repository

---

## 🛠️ STEP 1: CORE CONCEPTS & RESOURCES

### 🔹 Python Control Flow
1. **Loops**: Automating repetitive tasks.
   - `for` loop: Iterating over a sequence (e.g., `for i in range(5):`)
   - `while` loop: Running as long as a condition is true.
   - Control: `break` (exit loop), `continue` (skip to next iteration).
2. **Functions**: Reusable blocks of code.
   - Define: `def function_name(parameter):`
   - Return: `return result` (sends data back to the caller).
3. **Error Handling**: Preventing crashes when things go wrong.
   - `try:` (code that might fail)
   - `except ValueError:` (catches specific errors, like typing letters instead of numbers)

### 🔹 Primary Resource
- 📺 [FreeCodeCamp Python Course (1:00:00 → 2:30:00)](https://www.youtube.com/watch?v=rfscVS0vtbw&t=3600s)
- *Action*: Watch this segment, pause every 10 mins, and take handwritten notes.

---

## 💻 STEP 2: YOUR FIRST LOGIC SCRIPT (`calculator.py`)

### 📝 File: `calculator.py`
```python
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