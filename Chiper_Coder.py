
def Chiper(string: str, key: str):
    if (len(string) == 0): #Check message
        return "Bro, you forgot to enter a message"
    if (key == ''):
        return "Bro, you forgot to enter a key"
    if  not key.isdigit():
        if  not key.startswith('-') and key[1:].isdigit():
            return "Bro, you have submitted some cringe"

    key = int(key)


    ans = ''
    for i in range(len(string)):
        elemS = string[i]
        if (ord(elemS) >= 1040 and ord(elemS) < 1104) or elemS == "ё" or elemS == "Ё": # Russian
            language = 1
        elif (ord(elemS) >= 65 and ord(elemS) < 123): # English
            language = 2
        else:
            ans += elemS #other elemSs
            continue

        if language == 1: # Russian
            key %= 33
            alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
            alphabet_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
            if ((ord(elemS) >= 1072 and ord(elemS) < 1104) or elemS == "ё"): #LowerCase
                ans += alphabet[alphabet.find(elemS) + key]
            elif ((ord(elemS) >= 1040 and ord(elemS) < 1072)  or elemS == "Ё"): #UpperCase
                ans += alphabet_upper[alphabet_upper.find(elemS) + key]

        elif language == 2: # English
            key %= 26
            alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
            alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
            if ((ord(elemS) >= 97 and ord(elemS) < 123)): #LowerCase
                ans += alphabet[alphabet.find(elemS) + key]
            elif (ord(elemS) >= 65 and ord(elemS) < 97): #UpperCase
                ans += alphabet_upper[alphabet_upper.find(elemS) + key]
    return ans
