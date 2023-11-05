from tkinter import *
from tkinter import ttk
from Chiper_Coder import Chiper
from Visioner_Coder import Visioner
from Python_Decoder import DEVisioner


root = Tk()
root.title("coder")
root.geometry("600x400")

root.configure(bg='pink')

def clicked():
    s = message.get()
    k = key.get()
    textvariable = languages_var
    if languages_var.get() == "Шифровать":
        otv = Chiper(s, k)
    else:
        otv = Chiper(s, "-" + k)

    ans.configure(text=otv)

def clicked2():
    s = message4.get()
    k = key4.get()
    if languages_var2.get() == "Шифровать":
        otv = Visioner(s, k)
    else:
        otv = DEVisioner(s, k)
    ans4.configure(text=otv)

lbl0 = Label(root, text="Тут Шифр Цезаря. Я хочу:", bg = "pink")
lbl0.grid(column=0, row=0)



codes = ["Шифровать", "Дешифровать"]
# по умолчанию будет выбран первый элемент из codes
languages_var = StringVar(value=codes[0])

combobox = ttk.Combobox(textvariable=languages_var, values=codes, state="readonly")
combobox.grid(column=1, row=0)

lbl = Label(root, text="Введите текст:", bg = "pink")
lbl.grid(column=0, row=1)

message = Entry(root, width=60)
message.grid(column=1, row=1)
message.focus()

lbl2 = Label(root, text="Введите ключ:", bg = "pink")
lbl2.grid(column=0, row=2)
key = Entry(root, width=60)
key.grid(column=1, row=2)


btn = Button(root, textvariable=languages_var, command=clicked)
btn.grid(column=0, row=3)

lbl3 = Label(root, text="Вот ваш зашифрованный текст:", bg = "pink")
lbl3.grid(column=0, row=4)

ans = Label(root, text="", bg = "pink")
ans.grid(column=1, row=4)

lbl5 = Label(root, text="", bg = "pink")
lbl5.grid(column=0, row=5)

lbl6 = Label(root, text="", bg = "pink")
lbl6.grid(column=0, row=6)

lbl7 = Label(root, text="Тут шифр Виженера. Я хочу:", bg = "pink")
lbl7.grid(column=0, row=7)


codes2 = ["Шифровать", "Дешифровать"]
# по умолчанию будет выбран первый элемент из codes
languages_var2 = StringVar(value=codes[0])

combobox2 = ttk.Combobox(textvariable=languages_var2, values=codes2, state="readonly")
combobox2.grid(column=1, row=7)

lbl8 = Label(root, text="Введите текст:", bg = "pink")
lbl8.grid(column=0, row=8)

message4 = Entry(root, width=60)
message4.grid(column=1, row=8)

lbl9 = Label(root, text="Введите ключ:", bg = "pink")
lbl9.grid(column=0, row=9)

key4 = Entry(root, width=60)
key4.grid(column=1, row=9)

btn4 = Button(root, textvariable=languages_var2, command=clicked2)
btn4.grid(column=0, row=10)

lbl10 = Label(root, text="Вот ваш зашифрованный текст:", bg = "pink")
lbl10.grid(column=0, row=11)

ans4 = Label(root, text="", bg = "pink")
ans4.grid(column=1, row=11)

root.mainloop()