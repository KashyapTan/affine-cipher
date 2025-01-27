affine_cipher = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
    'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25
}

reverse_affine_cipher = {a: b for b, a in affine_cipher.items()}

plaintext = "howareyou"
numerical_plaintext = [affine_cipher[char] for char in plaintext]
print('Converting howareyou into corresponding numbers: ', numerical_plaintext)

def encrypt(x):
    return (5*x + 7) % 26

def decrypt(x):
    return (21*(x-7)) % 26

encrypted_numbers = [encrypt(num) for num in numerical_plaintext]
print('Encrypted numbers', encrypted_numbers)

encrypted_message = ''.join([reverse_affine_cipher[num] for num in encrypted_numbers])
print('Encrypted message:', encrypted_message)

decrypted_numbers = [decrypt(num) for num in encrypted_numbers]
print('Decrypted numbers', decrypted_numbers)

decrypted_message = ''.join([reverse_affine_cipher[num] for num in decrypted_numbers])
print('Decrypted message:', decrypted_message)