def sum(text, letter, size):
    count = 0
    for i in range(size):
        if letter == text[i]:
            count += 1
    return count


# Открытый текcт-------------------------------------------
with open("text.txt", "r", encoding='utf-8') as file:
    content = file.read()

text = list(content)
size_t = len(text)

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alphabet_size = len(alphabet)

alp = list(alphabet)

Open_text = [0] * alphabet_size
for i in range(alphabet_size):
    Open_text[i] = [0] * 2

for i in range(alphabet_size):
    Open_text[i][0] = alp[i]

for i in range(alphabet_size):
    Open_text[i][1] = sum(text, alp[i], size_t)

Open_text = sorted(Open_text, key=lambda x: x[1], reverse=True)
print(Open_text)

# Шифрованный текст-------------------------------------------
with open("cipher.txt", "r", encoding='utf-8') as file:
    content_cipher = file.read()

text_cipher = list(content_cipher)
text_cipher_final = list(content_cipher)
size = len(text_cipher)

Cipher_text = [0] * alphabet_size
for i in range(alphabet_size):
    Cipher_text[i] = [0] * 2

for i in range(alphabet_size):
    Cipher_text[i][0] = alp[i]

for i in range(alphabet_size):
    Cipher_text[i][1] = sum(text_cipher, alp[i], size)

Cipher_text = sorted(Cipher_text, key=lambda x: x[1], reverse=True)
print(Cipher_text)

with open("cipher.txt", "r", encoding='utf-8') as file:
    content_cipher = file.read()
print(content_cipher)
d = {}
for i, j in zip(Open_text, Cipher_text):
    d[j[0]] = i[0]
    print(str(i[0]) + " - " + str(j[0]))
content_cipher = content_cipher.lower()
new = []
for i in content_cipher:
    if d[i]:
        new.append(d[i])
    else:
        new.append(i)








