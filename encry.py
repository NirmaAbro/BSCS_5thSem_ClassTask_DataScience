# get input text message from the user
message = input("Enter a message: ")

# encrypt the message by shifting each letter by 1
encrypted_message = ""
for char in message:
        shifted_char = ((ord(char)+1))
       # shifted_char = chr((ord(char) - 97 + 1) % 26 + 97)
        encrypted_message += ord(shifted_char)
    
       # encrypted_message += shifted_char

          

# write encrypted message to a file
with open("encrypted_message.txt", "a") as f:
    f.write(encrypted_message)

print("Encrypted message written to encrypted_message.txt file.")