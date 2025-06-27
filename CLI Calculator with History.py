'''
Calculator with histor 
It is not a normal calculator with if else statement 
In this project we get the complete expression like 5+5
and we give 10 as output
We save the result in the txt file
We give the clear option to clear the history
We give option to perform another operation
'''

'''
Operations:
Input
Functions
Conditionals
File Handling
Loop
Expression , history , clear , exit
Math (Modulas , exponent) , (Multiple digits not only 2 digit expression)
'''
import os

filename = "history.txt"
if not os.path.exists(filename):
    open("history.txt", "w").close()

def show():
    with open("history.txt", "r") as f:
        lines = f.readlines()
        if len(lines) == 0:
            print("📄 History is empty.")
        else:
            for line in reversed(lines):
                print(line.strip())

def clear():
    with open("history.txt", "w") as f:
        pass
    print("History cleared.")

def save_to_history(expression, result):
    with open("history.txt", "a") as f:
        f.write(expression + " = " + str(result) + "\n")

def token(expression):
    expression = expression.replace(" ", "")
    tokens = []
    num = ""
    for ch in expression:
        if ch in "+-*/":
            tokens.append(num)
            tokens.append(ch)
            num = ""
        else:
            num += ch
    tokens.append(num)
    return tokens

def apply_operator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "Division by zero"
        return a / b

def calculate(expression):
    tokens = token(expression)
    for i in range(0, len(tokens), 2):
        tokens[i] = float(tokens[i])

    i = 1
    while i < len(tokens) - 1:
        if tokens[i] in "*/":
            result = apply_operator(tokens[i - 1], tokens[i + 1], tokens[i])
            if isinstance(result, str):
                return result
            tokens[i - 1:i + 2] = [result]
            i = 1
        else:
            i += 2

    i = 1
    while i < len(tokens) - 1:
        result = apply_operator(tokens[i - 1], tokens[i + 1], tokens[i])
        tokens[i - 1:i + 2] = [result]
        i = 1

    return tokens[0]

# ==== Main Program ====
while True:
    print("\n==== Calculator Menu ====")
    print("1. Calculate an expression (e.g., 10+20)")
    print("2. Show history")
    print("3. Clear history")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        expr = input("Enter expression: ").strip()
        result = calculate(expr)
        print("Result:", result)
        if isinstance(result, float) or isinstance(result, int):
            save_to_history(expr, result)

    elif choice == "2":
        show()

    elif choice == "3":
        clear()

    elif choice == "4":
        print("Exiting calculator. Allah Hafiz!")
        break

    else:
        print("Invalid option. Please select from 1 to 4.")































































































