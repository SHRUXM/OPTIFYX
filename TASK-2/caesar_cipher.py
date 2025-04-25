def encrypt(text, key):
        result = ''
        for char in text:
            if 'a' <= char <= 'z':
                start = ord('a')
            elif 'A' <= char <= 'Z':
                start = ord('A')
            else:
                result += char  # Keep non-letters as they are
                continue
            shifted_char = chr((ord(char) - start + key) % 26 + start)
            result += shifted_char
        return result

plaintext = input("Enter the message to encrypt: ")
key = int(input("Enter the encryption key (an integer): "))
ciphertext = encrypt(plaintext, key)
print("Encrypted message:", ciphertext)

def decrypt(ciphertext, key):
        return encrypt(ciphertext, -key)  # Reuse encrypt with a negative key

encrypted_text = input("Enter the message to decrypt: ")
key = int(input("Enter the decryption key (an integer): "))
decrypted_text = decrypt(encrypted_text, key)
print("Decrypted message:", decrypted_text)

def get_choice():
        while True:
            choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
            if choice in ('e', 'd'):
                return choice
            else:
                print("Invalid choice. Please enter 'e' or 'd'.")

choice = get_choice()

if choice == 'e':
    plaintext = input("Enter the message to encrypt: ")
    key = int(input("Enter the encryption key (an integer): "))
    ciphertext = encrypt(plaintext, key)
    print("Encrypted message:", ciphertext)
elif choice == 'd':
    encrypted_text = input("Enter the message to decrypt: ")
    key = int(input("Enter the decryption key (an integer): "))
    decrypted_text = decrypt(encrypted_text, key)
    print("Decrypted message:", decrypted_text)