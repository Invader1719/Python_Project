def Vernam_coder(string: str, key: str):
    '''
    В данной Функции Реализован Шифр Вернама.
    Я создал собственный алфавит на 128 элементах(Русский язык, Английский,
    Специальные символы, и цифры), замкнутый относительно
    XOR двух элементов.
    На входе подразумевается что длинна ключа и текста совпадают

    Этапы выполнения программы:
    1.1) Анализ ключа и строки на совпадение длинны
    1.2) Я создал уникальный массив, на индексах которого буду XORить
    2) Посимвольный парсинг входной строки и ключа. XOR
    3) Вывод Ответа

    :param string: Входной текст, который пользователь хочет
    закодировать шифром Вернама

    :param key: Ключ-Слово, Подразумевается что это
    английский/русский язык, Пунктаиционный символы, или цифры

    :return: Зашифрованный текст
    '''


    try:
        if (string[-1] == '\n'):
            string = string[:-1:]
    except:
        return "Bro, you forgot to enter a message"

    try:
        if (key[-1] == '\n'):
            key = key[:-1:]
    except:
        return "Bro, you forgot to enter a key"

    if (len(string) != len(key)):
        return "Bro, in Vernam Chiper Key and Input text must be the same length"


    a1 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyzǛǜǝǞǟǠǡǢǣǤǥǦǧǨǩǪǫǬǭǮǯǰǱǲǳǴǵǶǷǸǹǺǻǼʘǽǾǿȀȁȂȃȄȅȆȇȈȉȊȋȌȍȎ"
    A = list(a1)
    cnt = [" ", ".", "!", "?", "\n", ",", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    A += cnt

    ans = ''
    for i in range(len(string)):
        try:
            A.index(string[i])
            A.index(key[i])
        except:
            return "Bro please use numbers, Russian or English"
        ans += A[A.index(string[i])^A.index(key[i])]
    return ans
