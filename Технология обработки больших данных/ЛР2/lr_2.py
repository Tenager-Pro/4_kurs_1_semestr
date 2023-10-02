def count_words(file_name, substr, stop_words):
    word_count = 0

    # Открываем файл для чтения
    with open(file_name, 'r') as file:
        # Перебираем строки файла
        for line in file:
            # Разделяем строку на отдельные слова
            words = line.split()

            # Перебираем слова в строке
            for word in words:
                # Удаляем знаки препинания и приводим слово к нижнему регистру
                cleaned_word = word.strip('.,:;!?').lower()

                # Проверяем, начинается ли слово с заданной подстроки и не является ли оно стоп-словом
                if cleaned_word.startswith(substr) and cleaned_word not in stop_words:
                    word_count += 1

    return word_count
filename = "example.txt"  # Имя файла
substring = input("Введите подстроку: ")  # Заданная подстрока
stopwords = [] # Список стоп-слов
flag = True
while flag:
    stopword = input("Введите стоп слово, 0 конец : ")
    if stopword == "0":
        flag = False
        continue
    stopwords.append(stopword)  

result = count_words(filename, substring, stopwords)

output_filename = "word_count.txt"
with open(output_filename, 'w') as output_file:
    output_file.write(f"Количество слов, начинающихся с \"{substring}\", без стоп-слов: {result}\n")

print(f"Количество слов, начинающихся с \"{substring}\", без стоп-слов: {result}")
