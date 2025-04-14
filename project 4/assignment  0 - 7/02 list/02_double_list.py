def main():
    # Ask user to input numbers separated by spaces
    user_input = input("Enter numbers separated by spaces: ")

    # Convert the input string into a list of integers
    numbers = [int(num) for num in user_input.split()]

    # Double each number in the list
    for i in range(len(numbers)):
        numbers[i] *= 2

    print("Doubled List:", numbers)

if __name__ == '__main__':
    main()
