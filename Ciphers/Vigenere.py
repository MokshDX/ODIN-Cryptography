def encrypt(plain_text, key):
    encrypted_text = ""
    key_index = 0
    for char in plain_text:
        if char.isalpha():
            # Convert the key character to lowercase for simplicity
            key_char = key[key_index % len(key)].lower()
            shift = ord(key_char) - ord('a')
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text += encrypted_char
            key_index += 1
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(cipher_text, key):
    decrypted_text = ""
    key_index = 0
    for char in cipher_text:
        if char.isalpha():
            # Convert the key character to lowercase for simplicity
            key_char = key[key_index % len(key)].lower()
            shift = ord(key_char) - ord('a')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decrypted_text += decrypted_char
            key_index += 1
        else:
            decrypted_text += char
    return decrypted_text
