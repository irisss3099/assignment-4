def main():
    # Ask the user for a starting number
    curr_value = int(input("Enter a number: "))

    # Keep doubling the number until it reaches or exceeds 100
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

if __name__ == '__main__':
    main()
