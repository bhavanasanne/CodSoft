import random
import string

def generate_password(length):
    # Define the character sets for different complexity levels
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on complexity
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate a password by randomly selecting characters
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    try:
        # Prompt the user for the desired password length
        length = int(input("Enter the desired password length: "))
        
        if length < 8:
            print("Password length should be at least 8 characters.")
        else:
            # Generate and display the password
            password = generate_password(length)
            print("Generated Password: ", password)
    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")

if __name__ == "__main__":
    main()
