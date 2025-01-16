# Simple Calculator

def calculator():
    print("Simple Calculator")
    print("------------------")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Taking operation choice input
    choice = input("Enter choice (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please select a valid operation.")
        return

    # Taking two numbers as input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Performing calculation
    if choice == '1':
        result = num1 + num2
        operation = "Addition"
    elif choice == '2':
        result = num1 - num2
        operation = "Subtraction"
    elif choice == '3':
        result = num1 * num2
        operation = "Multiplication"
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        operation = "Division"
    
    # Displaying result
    print(f"{operation} result: {result}")
    print('\n')
        
        

while True:
  calculator()
  cal_again = input("Calculate again? (yes/no): ").lower()
  if cal_again != 'yes':
        print("Thankyou!")
        break
