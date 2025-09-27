import random
p = 23  
g = 5   
XA = random.randint(1, p-1)
XB = random.randint(1, p-1)
YA = pow(g, XA, p)
YB = pow(g, XB, p)
k_alice = pow(YB, XA, p)
k_bob = pow(YA, XB, p)

print(f"Alice's private key: {XA}")
print(f"Bob's private key: {XB}")
print(f"Alice's public key: {YA}")
print(f"Bob's public key: {YB}")
print(f"Shared secret key computed by Alice: {k_alice}")
print(f"Shared secret key computed by Bob: {k_bob}")
print("Shared secret keys match:", k_alice == k_bob)
