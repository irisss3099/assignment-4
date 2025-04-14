# Constants
PROMPT = "What do you want? "
JOKE = ("Here is a joke for you! Why did the computer go to therapy? "
        "Because it had too many bytes of emotional baggage.")
SORRY = "Sorry I only tell jokes."

def main():
    user_input = input(PROMPT)
    
    if user_input == "joke":
        print(JOKE)
    else:
        print(SORRY)

if __name__ == '__main__':
    main()
