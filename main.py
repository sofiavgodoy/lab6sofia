# Sofia Godoy
def encode(password):
    encoded_password = ""

    for digit in password:
        encoded_digit = str(int(digit) + 3)
        encoded_password += encoded_digit

    return encoded_password

def decode(encoded_password):
    decoded_password = ""

    for digit in encoded_password:
        decoded_digit = str(int(digit) - 3)
        decoded_password += decoded_digit

    return decoded_password

def main():
    while True:
        print("1. Encode Password")
        print("2. Decode Password")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            password = input("Enter an 8-digit password: ")
            if len(password) == 8 and password.isdigit():
                encoded_password = encode(password)
                print("Encoded Password:", encoded_password)
            else:
                print("Invalid input. Password must be an 8-digit integer.")
        elif choice == "2":
            encoded_password = input("Enter the encoded password: ")
            decoded_password = decode(encoded_password)
            print("Decoded Password:", decoded_password)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "_main_":
    main()