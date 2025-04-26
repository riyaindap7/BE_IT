while True:
    #creating a menu driven program
    print("Choose what to do:")
    print("1)encryption\n 2)decryption\n 3)brute force atttack\n 4)Exit")
    choice=int(input("Enter choice(1 to 4):"))
    #choice1 is to encrypt the given string
    if choice==1:
        alpha=input("Enter a string to encrypt:")
        key=int(input("Enter a key(1 to 25):"))
        Lalpha=alpha.lower()     #converting string to lower case
        encrypt=""               #Saving an empty string in encrypt
        for char in Lalpha:      #for each char in lower cased string   
            if char.isalpha():
                num=ord(char)-ord('a')   # mapping cahr to its equivaent number
                ciphered=(num+key)%26    # applying formula to encrypt using shift key value
                new_char=chr(ciphered+ord('a'))    #converting encrypted number to char again
                encrypt+=new_char.upper()    
            else:
                encrypt+=char
        print("The encrypted string is:"+encrypt)
    #choice2 is to decrypt the given string 
    elif choice==2:
        alpha=input("Enter a string to decrypt:") # applying same initial steps
        key=int(input("Enter a key(1 to 25):"))
        Lalpha=alpha.lower()
        decrypt=""
        for char in Lalpha:
            if char.isalpha():
                num=ord(char)-ord('a')
                deciphered=(num-key)%26      #applying formula to decrypt using shift key value
                new_char=chr(deciphered+ord('a'))
                decrypt+=new_char.upper()
            else:
                decrypt+=char
        print("The decrypted string is:"+decrypt)
    #choice3 is to decrypt the given string using brute force attack    
    elif choice==3:
        alpha=input("Enter a string to decrypt:")
        Lalpha=alpha.lower()
        for key in range(1,26):    #for all the key values from 1 to 26 decryption is performed
            decrypt=""
            for char in Lalpha:     
                if char.isalpha():
                    num=ord(char)-ord('a')
                    deciphered=(num-key)%26
                    new_char=chr(deciphered+ord('a'))
                    decrypt+=new_char.upper()
                else:
                    decrypt+=char
            print(f"for key{key} decrypted string is:{decrypt}")
    #to exit the code
    elif choice==4:
        print("exiting")
        break

    else:
        print("Enter a vaild choice")
