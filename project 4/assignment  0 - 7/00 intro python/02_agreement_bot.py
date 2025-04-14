def main():
    # Asking user to enter a question
    question = input("\033[1;3m What question would you like to ask?\033[0m ")

    # Asking for answer
    answer = input(f"{question} ")

    # Responding according to the question
    if "your name" in question.lower():
        print(f"My name is {answer}.")
    elif "your age" in question.lower():
        print(f"I am {answer} years old.")
    elif "your favorite color" in question.lower():
        print(f"My favorite color is {answer}.")
    elif "your hobby" in question.lower():
        print(f"My hobby is {answer}.")
    else:
        print(f"You asked: {question}")
        print(f"Your answer: {answer}")

if __name__ == '__main__':
    main()

