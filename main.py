affine_cipher = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
    'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25
}

reverse_affine_cipher = {a: b for b, a in affine_cipher.items()}

plaintext = "gezxds"
numerical_plaintext = [affine_cipher[char] for char in plaintext]
print('Converting solved into corresponding numbers: ', numerical_plaintext)

# def encrypt(x):
#     return (5*x + 7) % 26

# def decrypt(x):
#     return (21*(x-7)) % 26

# encrypted_numbers = [encrypt(num) for num in numerical_plaintext]
# print('Encrypted numbers', encrypted_numbers)

# encrypted_message = ''.join([reverse_affine_cipher[num] for num in encrypted_numbers])
# print('Encrypted message:', encrypted_message)

# decrypted_numbers = [decrypt(num) for num in encrypted_numbers]
# print('Decrypted numbers', decrypted_numbers)

# decrypted_message = ''.join([reverse_affine_cipher[num] for num in decrypted_numbers])
# print('Decrypted message:', decrypted_message)

# def solve_affine_keys():
#     # From equation 2, k2 = 14
#     k2 = 14
    
#     # Find k1 where 7k1 ≡ 25 (mod 26)
#     for k1 in range(26):
#         if (7 * k1) % 26 == 25:
#             return k1, k2
            
#     return None, None

# k1, k2 = solve_affine_keys()
# print(f"k1 = {k1}")
# print(f"k2 = {k2}")

# # Verify the solution
# print(f"Verification:")
# print(f"7k1 + k2 mod 26 = {(7*k1 + k2) % 26}")  # Should be 13
# print(f"0k1 + k2 mod 26 = {(0*k1 + k2) % 26}")  # Should be 14