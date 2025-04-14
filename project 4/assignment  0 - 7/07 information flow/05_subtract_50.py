def subtract_fifty(num):
    return num - 50  # Subtracts 50 from the given number

def main():
    number = int(input("Enter a number: "))  # Get user input
    result = subtract_fifty(number)  # Call the helper function
    print("Result after subtracting 50:", result)  # Print the result

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()