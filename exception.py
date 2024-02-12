while True:
    try:
        # Get user input for dividing two numbers
        dividend = float(input("Enter the dividend: "))
        divisor = float(input("Enter the divisor: "))

        # Perform division
        result = dividend / divisor

        # Display the result
        print(f"The result of {dividend} divided by {divisor} is {result}")

    except ValueError:
        print("Error: Please enter valid numbers for the dividend and divisor.")
        continue

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        continue

    except Exception as e:
        print(f"An error occurred: {e}")
        continue

    # Ask user if they want to continue
    response = input("Do you want to continue (yes/no)? ").lower()
    if response != 'yes':
        break
