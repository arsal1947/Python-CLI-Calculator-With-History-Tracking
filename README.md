# Python-CLI-Calculator-With-History-Tracking
A Python command-line calculator that supports basic arithmetic operations and maintains a persistent history of calculations in a text file. It includes options to view, clear, and save history. Ideal for beginner-level projects focused on file handling and expression evaluation.

# CLI Calculator with History (Python)

This is a simple command-line calculator written in Python. It evaluates basic arithmetic expressions and keeps a persistent history of all calculations in a text file. Users can view, clear, or save results during runtime.

## Features

- Calculate expressions (e.g., `10 + 20`, `15 / 3`)
- Handles division by zero with a warning
- Stores all successful calculations in `history.txt`
- View calculation history
- Clear history from the file
- Friendly CLI menu interface

## Technologies Used

- Python 3
- File Handling
- String Tokenization
- Arithmetic Expression Parsing

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/arsal1947/Python-CLI-Calculator.git
   cd Python-CLI-Calculator
Run the calculator:

python main.py
Use the menu to perform calculations or manage history:

1. Calculate an expression
2. Show history
3. Clear history
4. Exit

File Structure
main.py          # Main calculator logic
history.txt      # Stores all calculation history
README.md        # Project documentation

Sample Output

==== Calculator Menu ====
1. Calculate an expression (e.g., 10+20)
2. Show history
3. Clear history
4. Exit

Enter your choice (1-4): 1
Enter expression: 15 * 4
Result: 60.0
