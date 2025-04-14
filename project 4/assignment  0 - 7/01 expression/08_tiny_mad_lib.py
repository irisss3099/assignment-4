# Sentence beginning
SENTENCE_START: str = "The learning journey has been amazing. I picked up programming skills and built exciting things with Python"

def main():
    # Get the three inputs from the user
    adjective: str = input("Please type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter. ")

    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")

if __name__ == '__main__':
    main()