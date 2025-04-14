import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    # Generate and print N_NUMBERS random numbers within the given range
    for _ in range(N_NUMBERS):
        random_number = random.randint(MIN_VALUE, MAX_VALUE)
        print(random_number)

if __name__ == '__main__':
    main()

