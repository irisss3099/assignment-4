# Dictionary containing the gravity constants for each planet
gravity_constants = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.360,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.140
}

def main():
    # Milestone 1: Getting the user's weight on Earth
    weight_earth = float(input("Enter a weight on Earth: "))
    
    # Milestone 2: Get the planet name
    planet = input("Enter a planet: ")

    # Check if the planet is valid and calculate the equivalent weight
    if planet in gravity_constants:
        # Calculate the equivalent weight on the selected planet
        weight_planet = weight_earth * gravity_constants[planet]
        # Round the result to 2 decimal places
        print(f"The equivalent weight on {planet}: {round(weight_planet, 2)}")
    else:
        print("Invalid planet name. Please enter a valid planet.")

if __name__ == "__main__":
    main()
