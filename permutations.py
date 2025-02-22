import math

def simple_transposition_encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "")  # за бажанням можна видалити пробіли
    num_cols = len(key)
    num_rows = math.ceil(len(plaintext) / num_cols)
    # Заповнюємо матрицю символами, можна додати заповнювач, якщо необхідно
    matrix = []
    k = 0
    for r in range(num_rows):
        row = []
        for c in range(num_cols):
            if k < len(plaintext):
                row.append(plaintext[k])
            else:
                row.append("X")  # заповнювач, якщо потрібно
            k += 1
        matrix.append(row)

    # Отримуємо порядок стовпців, сортуємо індекси за значеннями літер ключа
    order = sorted(range(len(key)), key=lambda i: key[i])
    
    # Читаємо стовпці за порядком
    ciphertext = ""
    for i in order:
        for r in range(num_rows):
            ciphertext += matrix[r][i]
    return ciphertext

def simple_transposition_decrypt(ciphertext, key):
    num_cols = len(key)
    num_rows = math.ceil(len(ciphertext) / num_cols)
    num_shaded = (num_cols * num_rows) - len(ciphertext)
    # Порядок стовпців
    order = sorted(range(len(key)), key=lambda i: key[i])
    
    # Заповнюємо порожню матрицю
    matrix = [ [""] * num_cols for _ in range(num_rows) ]
    
    k = 0
    for idx in order:
        # Визначаємо кількість елементів у цьому стовпці
        col_len = num_rows
        if idx >= num_cols - num_shaded:
            col_len -= 1
        for r in range(col_len):
            matrix[r][idx] = ciphertext[k]
            k += 1

    # Читаємо рядками
    plaintext = ""
    for r in range(num_rows):
        plaintext += "".join(matrix[r])
    return plaintext

# Приклад
key_trans = "SECRET"
text_trans = "The artist is the creator of beautiful things"
enc_trans = simple_transposition_encrypt(text_trans, key_trans)
dec_trans = simple_transposition_decrypt(enc_trans, key_trans)
print("Простий перестановочний шифр:")
print("Зашифровано:", enc_trans)
print("Дешифровано:", dec_trans)
