def gronsfeld_encrypt(plaintext, key):
    ciphertext = ""
    key_len = len(key)
    key_index = 0

    for ch in plaintext:
        if ch.isalpha():
            p = ord(ch.lower()) - ord('a')
            k = int(key[key_index % key_len])

            c = (p + k) % 26
            ciphertext += chr(c + ord('a'))

            key_index += 1   # move key ONLY when letter is used
        else:
            ciphertext += ch

    return ciphertext


def gronsfeld_decrypt(ciphertext, key):
    plaintext = ""
    key_len = len(key)
    key_index = 0

    for ch in ciphertext:
        if ch.isalpha():
            c = ord(ch.lower()) - ord('a')
            k = int(key[key_index % key_len])

            p = (c - k) % 26
            plaintext += chr(p + ord('a'))

            key_index += 1   # same logic here
        else:
            plaintext += ch

    return plaintext


# Main Program
if __name__ == "__main__":
    print("1. Encrypt")
    print("2. Decrypt")

    choice = input("Enter choice (1/2): ")
    key = input("Enter numeric key (phone number): ")

    if choice == '1':
        plaintext = input("Enter plaintext: ")
        cipher = gronsfeld_encrypt(plaintext, key)
        print("Encrypted text:", cipher)

    elif choice == '2':
        ciphertext = input("Enter ciphertext: ")
        plain = gronsfeld_decrypt(ciphertext, key)
        print("Decrypted text:", plain)

    else:
        print("Invalid choice")