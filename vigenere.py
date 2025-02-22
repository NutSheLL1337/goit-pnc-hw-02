def generate_key(text, key):
    # Розширюємо ключ до довжини тексту
    key = key.upper()
    if len(text) == len(key):
        return key
    else:
        key_extended = list(key)
        for i in range(len(text) - len(key)):
            key_extended.append(key_extended[i % len(key)])
    return "".join(key_extended)

def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = generate_key(plaintext, key)
    ciphertext = ""
    for p, k in zip(plaintext, key):
        if p.isalpha():
            # Перетворюємо в числа (A=0, B=1, …)
            c = (ord(p) - ord('A') + ord(k) - ord('A')) % 26
            ciphertext += chr(c + ord('A'))
        else:
            ciphertext += p  # пропускаємо пробіли та пунктуацію
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = generate_key(ciphertext, key)
    plaintext = ""
    for c, k in zip(ciphertext, key):
        if c.isalpha():
            p = (ord(c) - ord('A') - (ord(k) - ord('A')) + 26) % 26
            plaintext += chr(p + ord('A'))
        else:
            plaintext += c
    return plaintext

# Приклад використання
key = "CRYPTOGRAPHY"
text = "THE ARTIST IS THE CREATOR OF BEAUTIFUL THINGS."
encrypted = vigenere_encrypt(text, key)
decrypted = vigenere_decrypt(encrypted, key)

print("Відкритий текст:", text)
print("Зашифрований текст:", encrypted)
print("Дешифрований текст:", decrypted)
