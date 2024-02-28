# read encrypted message from file
with open("encrypted_message.txt", "r+") as file:
    encrypted_message = file.read()

# initialize decrypted message
decrypted_message = ""

# shift each letter of the encrypted message back by 1 and add to decrypted message
for char in encrypted_message:
    if char.isalpha():
        original_char = chr((ord(char) - 97 - 1) % 26 + 97)
        decrypted_message += original_char
    else:
        decrypted_message += char

print("Decrypted message:", decrypted_message)
