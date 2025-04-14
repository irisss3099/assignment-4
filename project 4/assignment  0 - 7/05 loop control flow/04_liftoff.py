def main():
    print("What would you like to launch?")
    print("1. Numbers")
    print("2. Alphabets")
    print("3. Vowels")
    
    choice = input("Type 'numbers', 'alphabets', or 'vowels': ").strip().lower()

    if choice == "numbers":
        for i in range(10, 0, -1):
            print(i, end=" ")
        print("Liftoff... 🚀")

    elif choice == "alphabets":
        for letter in range(ord('z'), ord('a') - 1, -1):
            print(chr(letter), end=" ")
        print("Liftoff... 🚀")

    elif choice == "vowels":
        for letter in range(ord('u'), ord('a') - 1, -1):
            if chr(letter) in 'aeiou':
                print(chr(letter), end=" ")
        print("Liftoff... 🚀")

    else:
        print("Sorry, I didn't understand. Please choose: numbers, alphabets, or vowels.")

if __name__ == '__main__':
    main()
