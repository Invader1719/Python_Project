def visioner(string: str, key: str):
    '''
    В данной Функции Реализован Шифр Виженера. Этапы выполнения программы:
    1.1) Анализ ключа
    1.2) Если ключ меньше длинны текста, циклически продлеваю
    ключ до нужно длинны
    2) Посимвольный парсинг входной строки
    3.1) Для каждого элемента анализ языка. Обработка букв и
    остальных элементов
    3.2) (Если буква) Сдвиг буквы на нужную длину в алфавите
    по таблице Виженера. Реализовано на сдвиге по модулю в алфатие
    4) Вывод Ответа

    :param string: Входной текст, который пользователь хочет
    закодировать шифром Виженера

    :param key: Ключ-Слово, на который нужно сдвинуть буквы в алфавите.
    Проверка на совпадение языков. Подразумевается что здесь вводится
    текст без лишних символов в строку. То есть просто набор букв в
    правильном алфавите

    :return: Зашифрованный текст
    '''


    if (len(string) == 0) or (string == '\n'): #Check message
        return "Bro, you forgot to enter a message"
    if (key == '') or (key == '\n'):
        return "Bro, you forgot to enter a key"

    key = key[:-1:]
    #enlarge key up to message`s length
    n = len(key)
    if (len(key) < len(string)):
        i = 0
        while len(key) < len(string):
            i %= n
            elemS = key[i]
            if (((ord(elemS) >= 1040 and ord(elemS) < 1104) or elemS == "ё" or elemS == "Ё")
                    or (ord(elemS) >= 65 and ord(elemS) <= 90) or (ord(elemS) >= 97 and ord(elemS) <= 122)):
                key += key[i]
            i += 1

    ans = ''
    for i in range(len(string)):
        elemS = string[i]
        elemK = key[i]

        if (ord(elemS) >= 1040 and ord(elemS) <= 1103) or elemS == "ё" or elemS == "Ё": # Russian
            languageS = 1
        elif (ord(elemS) >= 65 and ord(elemS) <= 90) or (ord(elemS) >= 97 and ord(elemS) <= 122): # English
            languageS = 2
        else:
            ans += elemS #other elemSs
            continue

        if (ord(elemK) >= 1040 and ord(elemK) <= 1103) or elemK == "ё" or elemK == "Ё": # Russian
            languageK = 1
        elif (ord(elemK) >= 65 and ord(elemK) <= 90) or (ord(elemK) >= 97 and ord(elemK) <= 122): # English
            languageK = 2
        elif (elemK == ' ' or elemK == ',' or elemK == '!' or elemK == '.' or elemK == '?' or
              elemK == '(' or elemK == ')' or elemK == '[' or elemK == ']' or elemK.isdigit()):
            return "Bro, Key must consist only letters, without any punctuation, brackets, numbers or spaces"
        else:
            languageK = 4

        if languageS != languageK:
            return "Bro, you have mixed the languages"

        # Russian
        if languageS == 1:
            alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
            alphabet_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
            if ((ord(elemS) >= 1072 and ord(elemS) < 1104) or elemS == "ё"):  # LowerCase
                ans += alphabet[alphabet.find(elemS) + alphabet.find(key[i].lower())]
            elif ((ord(elemS) >= 1040 and ord(elemS) < 1072) or elemS == "Ё"):  # UpperCase
                ans += alphabet_upper[alphabet_upper.find(elemS) + alphabet_upper.find(key[i].upper())]

        # English
        elif languageS == 2:
            alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
            alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
            if ((ord(elemS) >= 97 and ord(elemS) < 123)): #LowerCase
                ans += alphabet[alphabet.find(elemS) + alphabet.find(key[i].lower())]
            elif (ord(elemS) >= 65 and ord(elemS) < 97):  # UpperCase
                ans += alphabet_upper[alphabet_upper.find(elemS) + alphabet_upper.find(key[i].upper())]

    return ans


def devisioner(string: str, key: str):
    '''
    В данной Функции Реализован ДЕшифр Виженера. Этапы выполнения программы:
    (Если у пользователя есть зашифрованый текст и ключ. А он хочет получить
     дешифрованный (искходный) текст)
    1.1) Анализ ключа
    1.2) Если ключ меньше длинны текста, циклически продлеваю
    ключ до нужно длинны
    2) Посимвольный парсинг входной строки
    3.1) Для каждого элемента анализ языка. Обработка букв и
    остальных элементов
    3.2) Проверка на сравнение, языков ключа и строки
    3.2) (Если буква) Сдвиг буквы в обратную сторону на нужную длину
    в алфавите по таблице Виженера. Реализовано на сдвиге по модулю
    4) Вывод Ответа

    :param string: Входной текст, который пользователь хочет
    декодировать шифром Виженера

    :param key: Ключ-Слово, на который нужно сдвинуть буквы в алфавите.
    Проверка на совпадение языков. Подразумевается что здесь вводится
    текст без лишних символов в строку. То есть просто набор букв в
    правильном алфавите

    :return: Зашифрованный текст
    '''


    if (len(string) == 0) or (string == '\n'): #Check message
        return "Bro, you forgot to enter a message"
    if (key == '') or (key == '\n'):
        return "Bro, you forgot to enter a key"

    #enlarge key up to message`s length
    key = key[:-1:]
    n = len(key)
    if (len(key) < len(string)):
        i = 0
        while len(key) < len(string):
            i %= n
            key += key[i]
            i += 1

    ans = ''
    for i in range(len(string)):
        # Check if Key and text are the same language
        elemS = string[i]
        elemK = key[i]

        #String elem language
        if (ord(elemS) >= 1040 and ord(elemS) <= 1103) or elemS == "ё" or elemS == "Ё": # Russian
            languageS = 1
        elif (ord(elemS) >= 65 and ord(elemS) <= 90) or (ord(elemS) >= 97 and ord(elemS) <= 122): # English
            languageS = 2
        else:
            ans += elemS #other elemSs
            continue

        # Key elem language
        if (ord(elemK) >= 1040 and ord(elemK) <= 1103) or elemK == "ё" or elemK == "Ё": # Russian
            languageK = 1
        elif (ord(elemK) >= 65 and ord(elemK) <= 90) or (ord(elemK) >= 97 and ord(elemK) <= 122): # English
            languageK = 2
        elif (elemK == ' ' or elemK == ',' or elemK == '!' or elemK == '.' or elemK == '?' or
              elemK == '(' or elemK == ')' or elemK == '[' or elemK == ']' or elemK.isdigit()):
            return "Bro, Key must consist only letters, without any punctuation, brackets, numbers or spaces"
        else:
            languageK = 4

        if languageS != languageK:
            return "Bro, you have mixed the languages"

        # Russian
        if languageS == 1:
            alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
            alphabet_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

            if ((ord(elemS) >= 1072 and ord(elemS) < 1104) or elemS == "ё"):  # LowerCase
                ans += alphabet[alphabet.find(elemS) - alphabet.find(key[i].lower()) + 33]
            elif ((ord(elemS) >= 1040 and ord(elemS) < 1072) or elemS == "Ё"):  # UpperCase
                ans += alphabet_upper[alphabet_upper.find(elemS) - alphabet_upper.find(key[i].upper()) + 33]

        # English
        elif languageS == 2:
            alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
            alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

            if ((ord(elemS) >= 97 and ord(elemS) < 123)): #LowerCase
                ans += alphabet[alphabet.find(elemS) - alphabet.find(key[i].lower()) + 26]
            elif (ord(elemS) >= 65 and ord(elemS) < 97):  # UpperCase
                ans += alphabet_upper[alphabet_upper.find(elemS) - alphabet_upper.find(key[i].upper()) + 26]

    return ans
