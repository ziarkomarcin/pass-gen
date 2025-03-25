import random
import string

# Function to generate a random password based on user preferences
def generate_password(min_lenght, numbers=True, special_characters=True):
    """
    Generates a random password with a specified minimum length.
    
    Parameters:
        min_lenght (int): The minimum length of the password.
        numbers (bool): Whether to include numbers in the password.
        special_characters (bool): Whether to include special characters in the password.
    
    Returns:
        str: A randomly generated password that meets the specified criteria.
    """
    # Define character pools
    letters = string.ascii_letters  # All uppercase and lowercase letters
    digits = string.digits          # All numeric digits (0-9)
    special = string.punctuation    # All special characters (!, @, #, etc.)

    # Start with letters and add digits/special characters if requested
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    # Initialize variables for password generation
    password = ""                   # The generated password
    meets_criteria = False          # Flag to check if password meets criteria
    has_number = False              # Flag to check if password contains a number
    has_special = False             # Flag to check if password contains a special character

    # Generate password until it meets the criteria and has the required length
    while not meets_criteria or len(password) < min_lenght:
        new_char = random.choice(characters)  # Randomly select a character
        password += new_char                  # Add the character to the password

        # Check if the new character is a number or special character
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        # Update the criteria flags based on user preferences
        meets_criteria = True
        if numbers:
            meets_criteria = has_number       # Ensure at least one number if required
        if special_characters:
            meets_criteria = meets_criteria and has_special  # Ensure at least one special character if required

    return password  # Return the generated password

# Get user input for password preferences
min_lenght = int(input("Enter the minimum lenght: "))  # Minimum password length
def get_yes_no_input(prompt):
    """
    Prompts the user for a 'y' or 'n' input and validates the response.
    
    Parameters:
        prompt (str): The message to display to the user.
    
    Returns:
        bool: True if the user inputs 'y', False if 'n'.
    """
    while True:
        user_input = input(prompt).lower()
        if user_input in ["y", "n"]:
            return user_input == "y"
        print("Invalid input. Please enter 'y' for yes or 'n' for no.")

# Example usage
has_number = get_yes_no_input("Do You want to have numbers? (y/n) ")  # Include numbers?
has_special = get_yes_no_input("Do You want to have special characters? (y/n) ")  # Include special characters?
# Generate the password based on user input
password = generate_password(min_lenght, has_number, has_special)
print("The generated password is: ", password)  # Display the generated password

# Save the password to a text file
file_path = "generated_passwords.txt"  # File to store generated passwords
with open(file_path, "a") as file:
    file.write(password + "\n")  # Append the password to the file
print(f"The password has been saved to {file_path}")  # Confirm the password was saved