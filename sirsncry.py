msg=input("enter any text :")
for ch in msg:
    ch2=chr(ord(ch)+1)
    print(ch2)
    
with open("encrypted_message.txt", "a") as f:
    f.write(msg)

print("Encrypted message written to encrypted_message.txt file.")