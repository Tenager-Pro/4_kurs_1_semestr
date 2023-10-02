
print('Метод Цезаря')

num=0
while num != '3':
    num=input('\nChoose ex. (1-2)\n1)Code\n2)Decode \nExit - 3\n >>>')
    if num=='1': 
        words=[]
        str1=input('Введите строку для кодирования: ')
        key=int(input('Введите ключ: '))
        for s in str1:
            print('Cимвол=',chr(ord(s)),'Код=',ord(s))
            if s!=' ':
                s=chr(ord(s)-key)
                words.append(s)
            else:
                s=chr(ord(s))
                words.append(s) 
        sentence = ''.join(words)
        print('Строка после кодирования: ',sentence)
    elif num=='2':
        words=[]
        str1=input('Введите строку для декодирования: ')
        key=int(input('Введите ключ: '))
        for s in str1:
            print('Cимвол=',chr(ord(s)),'Код=',ord(s))
            if s!=' ':
                s=chr(ord(s)+key)
                words.append(s)
            else:
                s=chr(ord(s))
                words.append(s) 
        sentence = ''.join(words)
        print('Строка после декодирования: ',sentence)
    elif num=='3':
        print('Good bye!')

 