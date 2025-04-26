def gcd(a,b):
    while b:
        a,b = b ,a % b
    return a

def mul_inv(e,phi):
    x0 , x1 = 0,1
    phi_original=phi
    while e>1:
        quotient= e // phi
        e ,phi = phi ,e %phi
        x0, x1= x1-quotient*x0,x0
    if x1<1:
        x1+=phi_original
    return x1


def key_gen(p,q,e):
    n=p*q
    phi=(p-1)*(q-1)
    if gcd(e,phi)!=1:
        raise ValueError("e and phi must be coprime")
    d= mul_inv(e,phi)
    return (e,n) ,(d,n)

def encrypt_message(message,key):
    e,n=key
    cipheretext=pow(message,e,n)
    return cipheretext

def decrypt_message(cipheretext,key):
    d,n=key
    plaintext=pow(cipheretext,d,n)
    return plaintext

def main():
    p=int(input("p:"))
    q=int(input("q:"))
    e=int(input("e:"))
    public, private=key_gen(p,q,e)
    print(f"public key is {public}")
    print(f"Private key is {private}")
    message=int(input("Enter the message to encrypt:"))
    cipheretext=encrypt_message(message,public)
    print(f"The encrypted message is:{cipheretext}")
    plaintext=decrypt_message(cipheretext,private)
    print(f"The decrypted message is:{plaintext}")

if __name__ == "__main__":
    main()
    
