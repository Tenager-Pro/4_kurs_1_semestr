def sum(text,letter,size):
    count = 0
    for i in range(size):
        if letter == text[i]:
            count += 1
    return count



#Открытый тектс-------------------------------------------
with open("text1.txt", "r", encoding='utf-8') as file:
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
print("Расшифрованный текст")
print(Open_text)

#Шифрованный текст-------------------------------------------
with open("text2.txt", "r", encoding='utf-8') as file:
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
print("Шифрованный текст")
print(Cipher_text)

for i, j in zip(Open_text, Cipher_text):
    print(i[0]+"-"+j[0])

filename = "text2.txt"
alphabet_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

with open(filename, 'r', encoding='utf-8') as file:
    ciphertext = file.read()
shift = 3
text = ''
for simbol in ciphertext:
    if simbol in alphabet_lower:
        text += alphabet_lower[(alphabet_lower.index(simbol) - shift) % len(alphabet_lower)]
    elif simbol in alphabet_upper:
        text += alphabet_upper[(alphabet_upper.index(simbol) - shift) % len(alphabet_upper)]
    else:
        text += simbol

print("Расшифрованный текст:")
print(text)