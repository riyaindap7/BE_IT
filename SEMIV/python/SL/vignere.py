def generate_key(text, key):
    key = list(key)
    if len(key) < len(text):
        key = key * (len(text) // len(key)) + key[:len(text) % len(key)]
    return ''.join(key)


def encrypt(text, key):
    cipher_text = []
    for i in range(len(text)):
        x = (ord(text[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return ''.join(cipher_text)


def decrypt(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return ''.join(orig_text)


def main():
    text = input("Enter text (uppercase): ").upper()
    key = input("Enter key (uppercase): ").upper()
    
    key = generate_key(text, key)
    encrypted_text = encrypt(text, key)
    print("Encrypted Text:", encrypted_text)
    
    decrypted_text = decrypt(encrypted_text, key)
    print("Decrypted Text:", decrypted_text)


if __name__ == "__main__":
    main()
