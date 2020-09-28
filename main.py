def encrypt(message, key):
    cipher = ""

    for c in message:
        number = ord(c) + key
        cipher += chr(number)
    return cipher

def decrypt(cipher, key):
    message = ""

    for c in cipher:
        number = ord(c) - key
        message += chr(number)
    return message

p = 29
alpha = 8

def get_public_key(alpha, p, private_key):
    return (alpha ** private_key) % p

def get_shared_key(public_key, private_key, p):
    return (public_key ** private_key) % p

alice_private_key = 12
bob_private_key = 7

alice_public_key = get_public_key(alpha, p, alice_private_key)
bob_public_key = get_public_key(alpha, p, bob_private_key)

alice_shared_key = get_shared_key(bob_public_key, alice_private_key, p)
bob_shared_key = get_shared_key(alice_public_key, bob_private_key, p)

alice_message = "Hello Bob"
alice_cipher = encrypt(alice_message, alice_shared_key)
bob_cipher = alice_cipher
print(alice_cipher)
bob_message = decrypt(bob_cipher, bob_shared_key)
print(bob_message)

print(alice_shared_key)
print(bob_shared_key)