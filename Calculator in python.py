def calculator():
    print("PYTHON CALCULATOR")

    # Initialize the result
    result = 0
    recent_input = None
    recent_operation = None
    f=1
    while True:
        if f==1:
            result = float(input("Enter the first number: "))
        # Display operation choices
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Clear ")
        print("6. All Clear ")
        print("7. Exit")
        
        # Get the user's choice
        choice = int(input("Choice (1/2/3/4/5/6/7): "))
        
        if choice == 7:  # Exit
            print(f"\nFinal result: {result}")
            break
        elif choice == 6:  # All Clear
            result = 0
            recent_input = None
            print("All inputs have been reset.")
            f=1
            continue
        elif choice == 5:  # Clear recent input
            if recent_input is not None and last_operation is not None:
                # Undo the last operation based on the stored recent input
                if last_operation == 1:  # Undo Addition
                    result -= recent_input
                elif last_operation == 2:  # Undo Subtraction
                    result += recent_input
                elif last_operation == 3:  # Undo Multiplication
                    if recent_input != 0:
                        result /= recent_input
                elif last_operation == 4:  # Undo Division
                    result *= recent_input
                
                print(f"{result}                                        Recent input has been cleared.")
                recent_input = None
                last_operation = None
            else:
                print("No recent input to clear.")
                f=0
            continue
        elif choice not in [1, 2, 3, 4]:
            print("Invalid choice! Please select a valid operation.")
            f=0
            continue
        
        # Ask for the next number
        try:
            next_number = float(input("Enter the next number: "))
            f=0
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        
        # Perform the selected operation
        if choice == 1:  # Addition
            tmp = result
            result += next_number
            operation = "Addition"
            sign='+'
            f=0
        elif choice == 2:  # Subtraction
            tmp = result
            result -= next_number
            sign='-'
            f=0
            operation = "Subtraction"
        elif choice == 3:  # Multiplication
            tmp = result
            result *= next_number
            sign='*'
            f=0
            operation = "Multiplication"
        elif choice == 4:  # Division
            tmp = result
            if next_number == 0:
                print("Error: Division by zero is not allowed. Please try again.")
                sign='/'
                f=0
            continue 
            result /= next_number
            operation = "Division"
        
        # Store the recent input for potential clearing
        recent_input = next_number
        last_operation = choice

        # Display the result after operation
        print(f" {tmp} {sign} {next_number}= {result}                                                 {operation} ")


calculator()
