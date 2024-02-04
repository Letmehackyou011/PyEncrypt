import webbrowser

def open_links(text):
    words = text.split()
    for word in words:
        if word.startswith('http://') or word.startswith('https://'):
            webbrowser.open(word)

text_with_links = "Follow me on Instagram https://instagram.com/thecoderxbro?igshid=YmMyMTA2M2Y="
open_links(text_with_links)


from cryptography.fernet import Fernet

def decrypt_code(key):
    encrypted_code = b'gAAAAABgUVehbZyVbcDNGXfQURWf74eojFVG8hCgH4_G1Zrc9tpiKjiXtyy_48F6Pm1js_DvB8FyDSYvz-MQQQQ'
    cipher_suite = Fernet(key)
    decrypted_code = cipher_suite.decrypt(encrypted_code).decode()
    exec(decrypted_code)

def generate_key():
    return Fernet.generate_key()

def encrypt_message(message, key):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message


logo = """
88\"\"Yb Yb  dP 888888 88b 88  dP\"\"b8 88\"\"Yb Yb  dP 88\"\"Yb 888888 
88__dP  YbdP  88__   88Yb88 dP   `\" 88__dP  YbdP  88__dP   88   
88\"\"\"    8P   88\"\"   88 Y88 Yb      88\"Yb    8P   88\"\"\"    88   
88      dP    888888 88  Y8  YboodP 88  Yb  dP    88       88   

by @Letmehackyou011
Follow me on Instagram @coderxbro
"""

print(logo)

key = generate_key()

while True:
    print("\nMenu:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. More tools")
    print("4. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        message_to_encrypt = input("Enter a message to encrypt: ")
        encrypted_message = encrypt_message(message_to_encrypt, key)
        print("Encrypted Message:", encrypted_message)
    
    elif choice == '2':
        encrypted_message = input("Enter the encrypted message: ")
        decrypted_message = decrypt_message(encrypted_message.encode(), key)
        print("Decrypted Message:", decrypted_message)
        
    elif choice == '3':
       def open_links(text):
           words = text.split()
           for word in words:
               if word.startswith('http://') or word.startswith('https://'):
                   webbrowser.open(word)

       text_with_links = "Watch more tools on GitHub page. Please follow me on Instagram https://github.com/Letmehackyou011"
       open_links(text_with_links)

    elif choice == '4':
        print("Thanks for using :)")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
