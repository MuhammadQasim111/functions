#  Python Calculator

This project is a ** Python Calculator** that performs basic arithmetic operations: addition, subtraction, multiplication, and division. It provides a user-friendly menu-driven interface and handles invalid inputs gracefully.

---

## Features

- **Operations Supported**:
  - Addition
  - Subtraction
  - Multiplication
  - Division (with error handling for division by zero)
- **Error Handling**:
  - Prevents invalid numeric inputs.
  - Provides feedback for invalid menu choices.
- **User-Friendly**: Offers a continuous loop for multiple calculations until the user chooses to exit.

---

## Functions

### `add(x, y)`
- **Description**: Adds two numbers.
- **Parameters**: 
  - `x`: First number.
  - `y`: Second number.
- **Returns**: The sum of `x` and `y`.

### `subtract(x, y)`
- **Description**: Subtracts the second number from the first.
- **Parameters**: 
  - `x`: First number.
  - `y`: Second number.
- **Returns**: The result of `x - y`.

### `multiply(x, y)`
- **Description**: Multiplies two numbers.
- **Parameters**: 
  - `x`: First number.
  - `y`: Second number.
- **Returns**: The product of `x` and `y`.

### `divide(x, y)`
- **Description**: Divides the first number by the second.
- **Parameters**: 
  - `x`: First number.
  - `y`: Second number.
- **Returns**: The result of `x / y`, or an error message if `y = 0`.

### `calculator()`
- **Description**: The main function that handles user input, displays the menu, and performs calculations.
- **Behavior**:
  - Prompts the user to select an operation or exit.
  - Validates user input.
  - Continuously loops until the user selects the exit option.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/Calculator.git
