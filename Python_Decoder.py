
def DEVisioner(string: str, key: str):

    if (len(string) == 0): #Check message
        return "Bro, you forgot to enter a message"
    if (len(key) == 0):
        return "Bro, you forgot to enter a key"

    #enlarge key up to message`s length
    n = len(key)
    if (len(key) < len(string)):
        i = 0
        while len(key) < len(string):
            i %= n
            key += key[i]
            i += 1

    ans = ''

    for i in range(len(string)):
        elemS = string[i]
        elemK = key[i]

        #Check if Key and text are the same language
        if ((ord(elemS) >= 1040 and ord(elemS) < 1104) or elemS == "ё" or elemS == "Ё") and (ord(elemK) >= 65 and ord(elemK) < 123):
            return "Bro, you have mixed Russian and English in your Key and Message"
        elif ((ord(elemK) >= 1040 and ord(elemK) < 1104) or elemK == "ё" or elemK == "Ё") and (ord(elemS) >= 65 and ord(elemS) < 123):
            return "Bro, you have mixed Russian and English in your Key and Message"
        elif not ((ord(elemK) >= 1040 and ord(elemK) < 1104) or elemK == "ё" or elemK == "Ё" or (ord(elemK) >= 65 and ord(elemK) < 123)):
            return "Bro, you have submitted some cringe"

        # Russian
        if (ord(elemS) >= 1040 and ord(elemS) < 1104) or elemS == "ё" or elemS == "Ё":
            alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
            alphabet_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

            if ((ord(elemS) >= 1072 and ord(elemS) < 1104) or elemS == "ё"):  # LowerCase
                ans += alphabet[alphabet.find(elemS) - alphabet.find(key[i].lower()) + 33]
            elif ((ord(elemS) >= 1040 and ord(elemS) < 1072) or elemS == "Ё"):  # UpperCase
                ans += alphabet_upper[alphabet_upper.find(elemS) - alphabet_upper.find(key[i].upper()) + 33]


        # English
        elif (ord(elemS) >= 65 and ord(elemS) < 123):
            alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
            alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

            if ((ord(elemS) >= 97 and ord(elemS) < 123)): #LowerCase
                ans += alphabet[alphabet.find(elemS) - alphabet.find(key[i].lower()) + 26]
            elif (ord(elemS) >= 65 and ord(elemS) < 97):  # UpperCase
                ans += alphabet_upper[alphabet_upper.find(elemS) - alphabet_upper.find(key[i].upper()) + 26]

        else:
            ans += elemS

    return ans
