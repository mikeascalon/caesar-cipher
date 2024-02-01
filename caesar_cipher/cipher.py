from caesar_cipher.corpus_loader import word_list

def encrypt(plain, shift):
    encrypted_text = ""

    for char in plain:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                shifted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            elif char.isupper():
                shifted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
        else:
            shifted_char = char  # If the character is not alphabetic, leave it unchanged

        encrypted_text += shifted_char

    return encrypted_text


def decrypt(encoded, shift):
     # To decrypt, simply call encrypt with the opposite (negative) shift
    return encrypt(encoded, -shift)

def crack(encrypted_text):
    common_words = set(word.lower() for word in word_list)
    max_word_count = 0
    best_shift = 0
    best_decryption = ""

    for shift in range(26):
        decrypted_text = decrypt(encrypted_text, shift)
        word_count = sum(word in decrypted_text.lower().split() for word in common_words)

        if word_count > max_word_count:
            max_word_count = word_count
            best_shift = shift
            best_decryption = decrypted_text

    # Return the best decryption only if it meets a minimum word count criterion
    # For example, you might require at least 1 or 2 common words to consider the decryption successful.
    # Adjust the minimum_word_count as needed based on your word list and test cases.
    minimum_word_count = 4  # or another number that makes sense for your application
    return best_decryption if max_word_count >= minimum_word_count else ""


