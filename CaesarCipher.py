def caesar_cipher(text, shift, mode='encrypt'):
    result = ''

    for char in text:
        if char.isalpha():
            
            base = ord('A') if char.isupper() else ord('a')
          
            if mode == 'encrypt':
                shifted = (ord(char) - base + shift) % 26 + base
            elif mode == 'decrypt':
                shifted = (ord(char) - base - shift) % 26 + base
            result += chr(shifted)
        else:
          
            result += char
    return result

def main():
    print("----- Caesar Cipher Program -----")
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (0-25): "))

    choice = input("Type 'e' to Encrypt or 'd' to Decrypt: ").lower()
    if choice == 'e':
        encrypted = caesar_cipher(message, shift, mode='encrypt')
        print(f"\nEncrypted Message: {encrypted}")
    elif choice == 'd':
        decrypted = caesar_cipher(message, shift, mode='decrypt')
        print(f"\nDecrypted Message: {decrypted}")
    else:
        print("Invalid choice! Please type 'e' or 'd'.")

if __name__ == "__main__":
    main()
