import logging

# Configure logging
logging.basicConfig(
    filename="calculator_log.txt",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Calculator function
def calculator():
    print("Simple Calculator (+, -, *, /)")

    try:
        num1 = float(input("Enter first number: "))
    except ValueError:
        logging.error("Invalid input: first number is not numeric")
        print("Invalid number!")
        return

    operator = input("Enter operator (+, -, *, /): ").strip()

    if operator not in ["+", "-", "*", "/"]:
        logging.error(f"Invalid operator entered: {operator}")
        print("Invalid operator!")
        return

    try:
        num2 = float(input("Enter second number: "))
    except ValueError:
        logging.error("Invalid input: second number is not numeric")
        print("Invalid number!")
        return

    # Perform operations
    try:
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                logging.error("Division by zero attempted")
                print("Error: Cannot divide by zero!")
                return
            result = num1 / num2

        logging.info(f"Calculation successful: {num1} {operator} {num2} = {result}")
        print("Result:", result)

    except Exception as e:
        logging.critical(f"Unexpected error occurred: {e}")
        print("Unexpected error occurred!")


# Run calculator
if __name__ == "__main__":
    calculator()
    print("\n✔ Run complete. Check calculator_log.txt for logs.")

