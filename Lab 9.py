def encode(password):
    encoded = ''.join(str((int(digit) + 3) % 10) for digit in password)
    return encoded


def decode(encoded_password):
    decoded = ''.join(str((int(digit) - 3) % 10) for digit in encoded_password)
    return decoded


def main():
    encoded_password = ""
    original_password = ""

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")

        if option == "1":
            original_password = input("Please enter your password to encode: ")
            if len(original_password) != 8 or not original_password.isdigit():
                print("Invalid password. Please ensure it is an 8-digit number.")
                continue
            encoded_password = encode(original_password)
            print("Your password has been encoded and stored!")

        elif option == "2":
            if not encoded_password:
                print("No password has been encoded yet.")
                continue
            print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")

        elif option == "3":
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
