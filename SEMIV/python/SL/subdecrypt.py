def decrypt(text,shift):
    decrypted_text=""
    for char in text:
        if char.isalpha():
            shifted=ord(char)-shift

            if char.islower():
                if shifted<ord('a'):
                    shifted += 26

            elif char.isupper():
                if shifted<ord('A'):
                    shifted +=26

            decrypted_text += chr(shifted)

        else:
            decrypted_text += char
    return decrypted_text

def main():
    text=input("Enter the text to decrypt")
    shift=int(input("Enter the shift value:"))

    decrypted=decrypt(text,shift)
    print("Decrypted:",decrypted)

if __name__=="__main__":
    main()
