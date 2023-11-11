# The Encryption Function
def cipher_encrypt(plain_text, key):
    encrypted = ""
    for c in plain_text:
        if c.isupper():
            c_index = ord(c) - ord('A')
            c_shifted = (c_index + key) % 26 + ord('A')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.islower():
            c_index = ord(c) - ord('a')
            c_shifted = (c_index + key) % 26 + ord('a')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.isdigit():
            c_new = (int(c) + key) % 10
            encrypted += str(c_new)
        else:
            encrypted += c
    return encrypted

# The Decryption Function
def cipher_decrypt(ciphertext, key):
    decrypted = ""
    for c in ciphertext:
        if c.isupper():
            c_index = ord(c) - ord('A')
            c_og_pos = (c_index - key) % 26 + ord('A')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.islower():
            c_index = ord(c) - ord('a')
            c_og_pos = (c_index - key) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.isdigit():
            c_og = (int(c) - key) % 10
            decrypted += str(c_og)
        else:
            decrypted += c
    return decrypted

def main():
    choice = input("Do you want to Encrypt or Decrypt? (E/D): ").upper()

    if choice == 'E':
        plain_text = input("Enter the plain text: ")
        key = int(input("Enter the key: "))
        ciphertext = cipher_encrypt(plain_text, key)
        print("Encrypted ciphertext:\n", ciphertext)

    elif choice == 'D':
        ciphertext = input("Enter the cipher text: ")
        key = int(input("Enter the key: "))
        decrypted_msg = cipher_decrypt(ciphertext, key)
        print("The decrypted message is:\n", decrypted_msg)

    else:
        print("Invalid choice. Please enter 'E' for Encrypt or 'D' for Decrypt.")

if __name__ == "__main__":
    main()
