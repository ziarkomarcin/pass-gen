import random
import string

def generate_password(min_lenght, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    password = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(password) < min_lenght:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return password

# Get user input
min_lenght = int(input("Enter the minimum lenght: "))
has_number = input("Do You want to have numbers? (y/n) ").lower() == "y"
has_special = input("Do You want to have special characters? (y/n) ").lower() == "y"

# Generate password
password = generate_password(min_lenght, has_number, has_special)
print("The generated password is: ", password)

# Save the password to a text file
file_path = "generated_passwords.txt"
with open(file_path, "a") as file:
    file.write(password + "\n")
print(f"The password has been saved to {file_path}")