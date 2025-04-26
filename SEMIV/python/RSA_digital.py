from sympy import mod_inverse, isprime

def generate_keys():
    # Get prime numbers p and q
    while True:
        p = int(input("Enter a prime number p: "))
        q = int(input("Enter a prime number q: "))
        if not (isprime(p) and isprime(q)):
            print("Both p and q must be prime numbers. Please try again.")
        elif p == q:
            print("p and q cannot be the same. Please try again.")
        else:
            break
    
    # Calculate n and phi(n)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Get public key e
    while True:
        e = int(input(f"Enter a public key 'e' such that 1 < e < {phi} and gcd(e, {phi}) = 1: "))
        if 1 < e < phi and gcd(e, phi) == 1:
            break
        else:
            print(f"Invalid 'e'. Make sure 1 < e < {phi} and gcd(e, {phi}) = 1. Please try again.")
    
    # Calculate private key d using Extended Euclidean Algorithm
    d = mod_inverse(e, phi)
    
    # Return public and private keys
    return (e, n), (d, n)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def sign_message(private_key, message):
    d, n = private_key
    # Ensure the message is treated as an integer
    message = int(message)
    S = pow(message, d, n)
    return S

def verify_signature(public_key, signature, original_message):
    e, n = public_key
    # Calculate M' using public key (M' = S^e mod n)
    m_prime = pow(signature, e, n)
    return m_prime == original_message

if __name__ == "__main__":
    print("RSA Key Generation:")
    public_key, private_key = generate_keys()
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")
    
    print("\nDigital Signature Generation:")
    message = int(input("Enter the message to sign (as an integer): "))
    signature = sign_message(private_key, message)
    print(f"Digital Signature: {signature}")
    
    print("\nSignature Verification:")
    verify_msg = int(input("Enter the original message to verify (as an integer): "))
    is_authentic = verify_signature(public_key, signature, verify_msg)
    
    if is_authentic:
        print("The message is authentic.")
    else:
        print("Message is altered, discard.")
