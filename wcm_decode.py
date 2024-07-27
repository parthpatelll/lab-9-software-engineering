#Decode function

def decode(password):
    decode_password = ''
    for char in password:
        char = int(char)
        char -= 3
        char = str(char)
        decode_password += char
    return decode_password
