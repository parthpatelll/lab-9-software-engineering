def encode(password):
    encoded_password = ''
    for char in password:
        encoded_password += str((int(char) + 3) % 10)
    return encoded_password

def decode(password):

    # partners implementation
    decode_password = ''
    for char in password:
        char = int(char)
        char -= 3
        char = str(char)
        decode_password += char
    return decode_password

def main():
    encoded_password = ''
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("Please enter an option: ")

        if option == '1':
            password = input("Please enter the password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")

        elif option == '2':
            if encoded_password:
                decoded_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            else:
                print("No password has been encoded yet!")

        elif option == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
