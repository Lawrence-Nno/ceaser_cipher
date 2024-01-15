alpha_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alpha_higher = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def encrypt(message):
    encrypted_msg = ""
    for char in message:
        # Checks if an inputted character is in lower case
        if char in alpha_lower:
            # Tracks both the index and the char in the alpha_lower list
            for index, letter in enumerate(alpha_lower):
                if char == letter:
                    # Ensures you don't get an index error and forces the count to continue from index zero
                    if index+shift_number >= len(alpha_lower):
                        new_index = (index+shift_number) - len(alpha_lower)
                    else:
                        new_index = index+shift_number
                    new_char = alpha_lower[new_index]
                    # Adds the encrypted character to the encrypted string
                    encrypted_msg += new_char
        # Checks if an inputted character is in higher case
        elif char in alpha_higher:
            # Tracks both the index and the char in the alpha_lower list
            for index, letter in enumerate(alpha_higher):
                if char == letter:
                    # Ensures you don't get an index error and forces the count to continue from index zero
                    if index+shift_number >= len(alpha_higher):
                        new_index = (index+shift_number) - len(alpha_higher)
                    else:
                        new_index = index+shift_number
                    new_char = alpha_higher[new_index]
                    # Adds the encrypted character to the encrypted string
                    encrypted_msg += new_char
        # Returns any character that isn't an alphabet as it is.
        else:
            encrypted_msg += char
    return encrypted_msg


def decrypt(message):
    decrypted_msg = ""
    for char in message:
        # Checks if an inputted character is in lower case
        if char in alpha_lower:
            # Tracks both the index and the character
            for index, letter in enumerate(alpha_lower):
                if char == letter:
                    # No need for further checks as there is no possibility of an index error or mis-shift
                    new_char = alpha_lower[index-shift_number]
                    decrypted_msg += new_char
        # Checks if an inputted character is in higher case
        elif char in alpha_higher:
            # Tracks both the index and the character
            for index, letter in enumerate(alpha_higher):
                if char == letter:
                    new_char = alpha_higher[index-shift_number]
                    decrypted_msg += new_char
        # Returns any character that isn't an alphabet as it is.
        else:
            decrypted_msg += char
    return decrypted_msg


still_encoding = True
while still_encoding:
    # To ensure either 'encode' or 'decode' is inputted
    while True:
        action = input("Type 'encode' to encrypt and 'decode' to decrypt:\n")
        if action.lower() != 'encode' and action.lower() != 'decode':
            print("Enter either 'encode' or 'decode' to encrypt or decrypt.")
        else:
            break

    # To ensure an integer is inputted as shift number
    while True:
        try:
            shift_number = int(input("Enter the Shift Number:\n"))
        except ValueError:
            print("Shift Number should be an Integer")
        else:
            break

    # Stores the input on a variable named 'message'
    message = input("Type your message:\n")

    # Chooses which function to use depending on the chosen 'action' above
    if action.lower() == 'encode':
        print(f"Here is your encrypted message: {encrypt(message)}")
    elif action.lower() == 'decode':
        print(f"Here is your decrypted message: {decrypt(message)}")

    # Checks if the user wants to keep encoding/decoding
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if again.lower() == 'yes':
        pass
    else:
        still_encoding = False


