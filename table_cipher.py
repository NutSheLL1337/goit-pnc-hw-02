plain_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
keyword = "MATRIX"
key_unique = ""
for ch in keyword.upper():
    if ch not in key_unique:
        key_unique += ch

cipher_alphabet = key_unique
for ch in plain_alphabet:
    if ch not in cipher_alphabet:
        cipher_alphabet += ch

def table_encrypt(text):
    result = ""
    for ch in text.upper():
        if ch in plain_alphabet:
            idx = plain_alphabet.index(ch)
            result += cipher_alphabet[idx]
        else:
            result += ch
    return result

def table_decrypt(ciphertext):
    result = ""
    for ch in ciphertext.upper():
        if ch in cipher_alphabet:
            idx = cipher_alphabet.index(ch)
            result += plain_alphabet[idx]
        else:
            result += ch
    return result

# Приклад
text_table = "The artist is the creator of beautiful things"
encrypted_table = table_encrypt(text_table)
decrypted_table = table_decrypt(encrypted_table)
print("Табличний шифр:")
print("Зашифровано:", encrypted_table)
print("Дешифровано:", decrypted_table)
