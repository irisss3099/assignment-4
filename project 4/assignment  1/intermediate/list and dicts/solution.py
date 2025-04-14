def add_to_list(lst, number):
    lst.append(number)
    return lst

def remove_from_list(lst, number):
    if number in lst:
        lst.remove(number)
        return lst
    else:
        return "Number not found in the list."

def find_in_list(lst, number):
    if number in lst:
        return f"Number {number} is at index {lst.index(number)}."
    else:
        return f"Number {number} not found."

def number_list_operations():
    num_list = [10, 20, 30, 40, 50]  # Initial list of numbers
    print("Current list:", num_list)
    print("Choose an operation: add, remove, find")
    operation = input("Enter operation: ")

    if operation == "add":
        number = int(input("Enter number to add: "))
        print("Updated list:", add_to_list(num_list, number))
    elif operation == "remove":
        number = int(input("Enter number to remove: "))
        print("Updated list:", remove_from_list(num_list, number))
    elif operation == "find":
        number = int(input("Enter number to find: "))
        print(find_in_list(num_list, number))
    else:
        print("Invalid operation.")

number_list_operations()

