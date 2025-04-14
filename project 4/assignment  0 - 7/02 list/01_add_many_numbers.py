def sum_of_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def main():
    numbers_list = []

    print("Enter at least 5 different numbers:")

    while len(numbers_list) < 5:
        try:
            num = int(input(f"Enter number {len(numbers_list) + 1}: "))
            numbers_list.append(num)
        except ValueError:
            print("Please enter a valid number.")

    result = sum_of_numbers(numbers_list)
    print("List:", numbers_list)
    print("Sum of numbers:", result)

if __name__ == '__main__':
    main()

