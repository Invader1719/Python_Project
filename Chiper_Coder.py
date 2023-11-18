def chipper(string: str, key: str):
    '''
    В данной Функции Реализован Шифр Цезаря. Этапы выполнения программы:

    1) Анализ ключа
    2) Посимвольный парсинг входной строки
    3.1) Для каждого элемента анализ языка. Обработка букв и
    остальных элементов
    3.2) (Если буква) Сдвиг буквы на нужную длину в алфавите
    4) Вывод Ответа

    :param string: Входной текст, который пользователь хочет
    закодировать шифром Цезаря на сдвиг равный key

    :param key: Ключ, на который нужно сдвинуть буквы в алфавите.
    Передается как строка, так как там может быть любой текст
    Если число то все нормально, если нет то этот случай
    рассматривается отдельно.

    :return: Зашифрованный текст
    '''


    # Check message
    if (len(string) == 0) or (string == '\n'):
        return "Bro, you forgot to enter a message"
    if (key == '') or (key == '\n'):
        return "Bro, you forgot to enter a key"
    try:
        int(key)
    except:
        return "Bro, Key must be an integer"

    key = int(key)

    ans = ''
    for i in range(len(string)):

        elemS = string[i]
        if (ord(elemS) >= 1040 and ord(elemS) <= 1103)\
or elemS == "ё" or elemS == "Ё": # Russian
            language = 1
        elif (ord(elemS) >= 65 and ord(elemS) <= 90)\
or (ord(elemS) >= 97 and ord(elemS) <= 122): # English
            language = 2
        else:
            ans += elemS #other elemSs
            continue

        if language == 1: # Russian
            key_cur = key % 33
            alphabet = "абвгдеёжзийклмнопрстуфхцчш\
щъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
            alphabet_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУ\
ФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
            if ((ord(elemS) >= 1072 and ord(elemS) < 1104)\
or elemS == "ё"): #LowerCase
                ans += alphabet[alphabet.find(elemS) + key_cur]
            elif ((ord(elemS) >= 1040 and ord(elemS) < 1072)\
or elemS == "Ё"): #UpperCase
                ans += alphabet_upper[alphabet_upper.find(elemS) + key_cur]

        elif language == 2: # English
            key_cur = key % 26
            alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
            alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ\
ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            if ((ord(elemS) >= 97 and ord(elemS) < 123)): #LowerCase
                ans += alphabet[alphabet.find(elemS) + key_cur]
            elif (ord(elemS) >= 65 and ord(elemS) <= 90): #UpperCase
                ans += alphabet_upper[alphabet_upper.find(elemS) + key_cur]

    return ans


def chipper_hack(string: str):
    '''
    В данной Функции Реализован взлом Шифра Цезаря.
    P.S. Не гарантируется Адекватный взлом при длине
    текста менее 1000 символов или слишком сильно
    намешан русский и английский языки. Когда Их
    немного, например статья из Википедии, все
    работает корректно)

    Этапы выполнения программы:

    1) Посимвольный парсинг входной строки
    2) Парсинг строки
    3) Если символ буква. То подсчитываем ее количество в словарь
    4.1) Учитывая что в русском языке частота встречаемости буквы "о"
    в русском языке 11%, а после нее идут три буквы по 8%, разумно
    угадывать ключ по 1 букве.
    4.2) В английском языке буква "е" встречается 12.5%, а после нее
    также идут три буквы по 8%, разумно угадывать ключ по 1 букве.
    5) Вывод Ответа

    :param string: Входной текст, который пользователь хочет
    взломать.

    :return: Взломанный текст
    '''


    counter = dict()
    n = len(string)
    string = string.lower()

    #Count letters in string
    for i in range(n):
        elemS = string[i]
        if (((ord(elemS) >= 1040 and ord(elemS) < 1104)\
or elemS == "ё" or elemS == "Ё") or
                (ord(elemS) >= 65 and ord(elemS) <= 90)\
or (ord(elemS) >= 97 and ord(elemS) <= 122)):
            try:
                counter[string[i]] += 1
            except:
                counter[string[i]] = 1
    A = list(counter.items())
    A.sort(key = lambda n: n[1], reverse = True)
    elemS = A[0][0]

    #trying to guess language
    if (ord(elemS) >= 1040 and ord(elemS) < 1104)\
or elemS == "ё" or elemS == "Ё":  # Russian
        language = 1
    elif (ord(elemS) >= 65 and ord(elemS) <= 90)\
or (ord(elemS) >= 97 and ord(elemS) <= 122):  # English
        language = 2

    if language == 1:  # Russian
        alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяа\
бвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        alphabet_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ\
АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        if ((ord(elemS) >= 1072 and ord(elemS) < 1104)\
or elemS == "ё"):  # LowerCase
            key = alphabet.find(elemS) - alphabet.find("о")
        elif ((ord(elemS) >= 1040 and ord(elemS) < 1072) or elemS == "Ё"):  # UpperCase
            key = alphabet_upper.find(elemS) - alphabet_upper.find("О")

    elif language == 2:  # English
        alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if ((ord(elemS) >= 97 and ord(elemS) < 123)):  # LowerCase
            key = alphabet.find(elemS) - 4
        elif (ord(elemS) >= 65 and ord(elemS) < 97):  # UpperCase
            key = alphabet_upper.find(elemS) - 4

    return chipper(string, str(-key))
