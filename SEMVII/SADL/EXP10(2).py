def left_rotate(value, bits):
    """Left rotate a 32-bit integer."""
    return ((value << bits) | (value >> (32 - bits))) & 0xFFFFFFFF

def sha1(message):
    # Convert message to bytes
    if isinstance(message, str):
        message = message.encode()

    original_bit_length = len(message) * 8

    # Padding
    message += b'\x80'
    while ((len(message) * 8) % 512) != 448:
        message += b'\x00'

    # Append original length as 64-bit big-endian
    message += original_bit_length.to_bytes(8, 'big')

    # Initial hash values
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # Process 512-bit chunks
    for chunk_start in range(0, len(message), 64):
        chunk = message[chunk_start:chunk_start + 64]
        w = [0] * 80

        # Break chunk into sixteen 32-bit big-endian words
        for i in range(16):
            w[i] = int.from_bytes(chunk[i*4:(i*4)+4], 'big')

        # Extend to 80 words
        for i in range(16, 80):
            w[i] = left_rotate(w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16], 1)

        # Initialize working vars
        a, b, c, d, e = h0, h1, h2, h3, h4

        # Main loop
        for i in range(80):
            if i < 20:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif i < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif i < 60:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (left_rotate(a, 5) + f + e + k + w[i]) & 0xFFFFFFFF
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        # Add this chunk's hash to result
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    # Return final hash as hex string
    return f"{h0:08x}{h1:08x}{h2:08x}{h3:08x}{h4:08x}"

# Example usage
msg1 = "Hello World"
msg2 = "Hello World!"

print("Input 1:", msg1)
print("SHA-1 Hash 1:", sha1(msg1))
print("\nInput 2:", msg2)
print("SHA-1 Hash 2:", sha1(msg2))
