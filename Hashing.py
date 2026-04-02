def hash_function(text):
    result = ""

    for i in range(len(text)):
        ch = text[i]

        if ch.isalpha():
            ascii_val = ord(ch.lower())  # ensure consistency

            # hashing formula
            H = (ascii_val + 3*i + 7) % 26
            digit = H % 10

            result += str(digit)
        else:
            result += ch  # keep spaces/symbols

    return result


# Example usage
if __name__ == "__main__":
    text = input("Enter text to hash: ")

    hashed = hash_function(text)
    print("Hashed output:", hashed)