import string
import random


def generate_password(length):
    # Define possible characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    try:
        # User input for password length
        length = int(input("Enter the desired length for the password: "))
        if length <= 0:
            print("Password length should be a positive integer.")
            return

        # Generate and display the password
        password = generate_password(length)
        print(f"Generated password: {password}")

    except ValueError:
        print("Invalid input! Please enter a valid number.")


if __name__ == "__main__":
    main()
