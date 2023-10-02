import math


def fast_pow(x, y):
    if y == 0:
        return 1
    if y == -1:
        return 1. / x
    p = fast_pow(x, y // 2)
    p *= p
    if y % 2:
        p *= x
    return p


def keygen(p, q):
    n = p*q
    euler = (p - 1) * (q - 1)

    e = 0
    i = 2
    while i < euler:
        e = math.gcd(euler, i)
        if e == 1:
            e = i
            break
        i += 1

    d = 0
    i = 2
    while i < n:
        if (i * e) % euler == 1:
            d = i
            break
        i += 1

    keys = [e, d, n]
    return keys


def encode(message, e, n):
    return fast_pow(message, e) % n


def decode(message, d, n):
    return fast_pow(message, d) % n


alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
p = int(input("Введите простое число p: "))
q = int(input("Введите простое число q: "))
keys = keygen(p, q)
message = input("Введите сообщение для расшифровки: ")
symbols = list(message)

for i in range(0, len(symbols)):
    for j in range(0, len(alphabet)):
        if symbols[i] == alphabet[j]:
            symbols[i] = j + 1

for i in range(0, len(symbols)):
    symbols[i] = encode(symbols[i], keys[0], keys[2])

print(symbols)

for i in range(0, len(symbols)):
    symbols[i] = decode(symbols[i], keys[1], keys[2])

for i in range(0, len(symbols)):
    for j in range(0, len(alphabet)):
        if symbols[i] == j + 1:
            symbols[i] = alphabet[j]

print(symbols)


#Диффи-Хеллман
q = 17
a = 3
Xa = 6
Yb = 11
K = 12

print(math.pow(a, Xa) % q)
