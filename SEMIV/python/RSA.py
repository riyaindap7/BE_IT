from sympy import mod_inverse
import math

# Function to factorize n into p and q
def factorize_n(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i, n // i
    raise ValueError("Failed to factorize n")

# Function to generate RSA parameters given public key (e, n)
def generate_rsa_params(e, n):
    # Factorize n into p and q
    p, q = factorize_n(n)
    
    # Compute φ(n)
    phi = (p - 1) * (q - 1)
    
    # Compute the private key d
    d = mod_inverse(e, phi)
    
    return p, q, phi, d

# Function to encrypt a message using RSA
def rsa_encrypt(message, e, n):
    return pow(message, e, n)

# Function to decrypt a message using RSA
def rsa_decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)

# Main execution
if __name__ == "__main__":
    # User input for Party A's public key
    e_A, n_A = map(int, input("Enter Party A's public key (e_A, n_A) separated by a space: ").split())
    
    # User input for Party B's public key
    e_B, n_B = map(int, input("Enter Party B's public key (e_B, n_B) separated by a space: ").split())
    
    # Generate RSA parameters for Party A
    p_A, q_A, phi_A, d_A = generate_rsa_params(e_A, n_A)
    print(f"Party A's parameters:")
    print(f"p_A: {p_A}")
    print(f"q_A: {q_A}")
    print(f"φ(n_A): {phi_A}")
    print(f"Private key d_A: {d_A}")

    # Generate RSA parameters for Party B
    p_B, q_B, phi_B, d_B = generate_rsa_params(e_B, n_B)
    print(f"Party B's parameters:")
    print(f"p_B: {p_B}")
    print(f"q_B: {q_B}")
    print(f"φ(n_B): {phi_B}")
    print(f"Private key d_B: {d_B}")

    # Example encryption and decryption
    # A sends message M = 5 to B
    message_from_A = int(input("Enter the message M to be sent from A to B: "))
    ciphertext_A_to_B = rsa_encrypt(message_from_A, e_B, n_B)
    print(f"Ciphertext from A to B: {ciphertext_A_to_B}")

    # B decrypts the message
    decrypted_message_B = rsa_decrypt(ciphertext_A_to_B, d_B, n_B)
    print(f"Decrypted message received by B: {decrypted_message_B}")

    # B sends message M = 3 to A
    message_from_B = int(input("Enter the message M to be sent from B to A: "))
    ciphertext_B_to_A = rsa_encrypt(message_from_B, e_A, n_A)
    print(f"Ciphertext from B to A: {ciphertext_B_to_A}")

    # A decrypts the message
    decrypted_message_A = rsa_decrypt(ciphertext_B_to_A, d_A, n_A)
    print(f"Decrypted message received by A: {decrypted_message_A}")
