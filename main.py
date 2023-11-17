import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from Chiper_Coder import Chiper
from Chiper_Coder import Chiper_hack
from Visioner_Coder import Visioner
from Visioner_Coder import DEVisioner
from Vernam import Vernam_coder

def openFile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),)
        )
    tf = open(tf, 'r')
    data = tf.read()
    message.insert(tk.END, data)
    tf.close()

def openFile2():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),)
        )
    tf = open(tf, 'r')
    data = tf.read()
    message4.insert(tk.END, data)
    tf.close()

def openFile3():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),)
        )
    tf = open(tf, 'r')
    data = tf.read()
    messagev1.insert(tk.END, data)
    tf.close()

def clicked():
    s = message.get(1.0, tk.END)
    k = key.get(1.0, tk.END)
    if languages_var.get() == "Шифровать":
        otv = Chiper(s, k)
    elif languages_var.get() == "Взломать!":
        otv = Chiper_hack(s)
    else:
        print(s, list("-" + k))
        otv = Chiper(s, "-" + k)

    ans.delete(1.0, tk.END)
    ans.insert(1.0, otv)

def clicked2():
    s = message4.get(1.0, tk.END)
    k = key4.get(1.0, tk.END)
    if languages_var2.get() == "Шифровать":
        otv = Visioner(s, k)
    else:
        otv = DEVisioner(s, k)
    ans_Visioner.delete(1.0, tk.END)
    ans_Visioner.insert(1.0, otv)

def clicked3():
    s = messagev1.get(1.0, tk.END)
    k = keyv2.get(1.0, tk.END)
    otv = Vernam_coder(s, k)
    ans_Vernam.delete(1.0, tk.END)
    ans_Vernam.insert(1.0, otv)

root = tk.Tk()
root.title("coder")
root.geometry("1500x800")
root.configure(bg='pink')

bg = tk.PhotoImage(file="Rayan_Gosling.png")
label1 = tk.Label(root, image=bg)
label1.place(x=0, y=0)

chiper_intro = tk.Label(root, text="Тут Шифр Цезаря. Я хочу:", font='Times 12', bg = "pink")
chiper_intro.grid(column=0, row=0)

codes = ["Шифровать", "Дешифровать", "Взломать!"] #tk.Button
# по умолчанию будет выбран первый элемент из codes
languages_var = tk.StringVar(value=codes[0])

combobox = ttk.Combobox(textvariable=languages_var, values=codes, state="readonly")
combobox.grid(column=1, row=0)

lbl = tk.Label(root, text="Введите текст:", font='Times 12', bg = "pink")
lbl.grid(column=0, row=1)

message = tk.Text(width=60, height=4)
message.grid(column=1, row=1)

scroll = tk.Scrollbar(command=message.yview)
scroll.grid(column=2, row=1)

message.config(yscrollcommand=scroll.set)
scroll.config(command=message.yview)

tk.Button(root, text="Open File", command=openFile).grid(column=0, row=3)

lbl2 = tk.Label(root, text="Введите ключ:", font='Times 12', bg = "pink")
lbl2.grid(column=0, row=4)

key = tk.Text(width=60, height=2)
key.grid(column=1, row=4)

btn = tk.Button(root, textvariable=languages_var, command=clicked)
btn.grid(column=0, row=5)

lbl3 = tk.Label(root, text="Вот ваш зашифрованный текст:", font='Times 12', bg = "pink")
lbl3.grid(column=0, row=6)

ans = tk.Text(width=60, height=4)
ans.grid(column=1, row=6)

scroll2 = tk.Scrollbar(command=ans.yview)
scroll2.grid(column=2, row=6)

ans.config(yscrollcommand=scroll2.set)

lbl7 = tk.Label(root, text="Тут шифр Виженера. Я хочу:", font='Times 12', bg = "pink")
lbl7.grid(column=0, row=7)

codes2 = ["Шифровать", "Дешифровать"]
# по умолчанию будет выбран первый элемент из codes
languages_var2 = tk.StringVar(value=codes2[0])

combobox2 = ttk.Combobox(textvariable=languages_var2, values=codes2, state="readonly")
combobox2.grid(column=1, row=7)

lbl8 = tk.Label(root, text="Введите текст:", font='Times 12', bg = "pink")
lbl8.grid(column=0, row=8)


message4 = tk.Text(width=60, height=4)
message4.grid(column=1, row=8)

scroll3 = tk.Scrollbar(command=message.yview)
scroll3.grid(column=2, row=8)

message4.config(yscrollcommand=scroll3.set)
tk.Button(root, text="Open File", command=openFile2).grid(column=0, row=9)

lbl9 = tk.Label(root, text="Введите ключ:", font='Times 12', bg = "pink")
lbl9.grid(column=0, row=10)

key4 = tk.Text(width=60, height=2)
key4.grid(column=1, row=10)

btn4 = tk.Button(root, textvariable=languages_var2, command=clicked2)
btn4.grid(column=0, row=11)

lbl10 = tk.Label(root, text="Вот ваш зашифрованный текст:", font='Times 12', bg = "pink")
lbl10.grid(column=0, row=12)

ans_Visioner = tk.Text(width=60, height=4)
ans_Visioner.grid(column=1, row=12)

scroll4 = tk.Scrollbar(command=message.yview)
scroll4.grid(column=2, row=12)

ans_Visioner.config(yscrollcommand=scroll4.set)

lblv1 = tk.Label(root, text="Тут шифр Вернама. Я хочу:", font='Times 12', bg = "pink")
lblv1.grid(column=0, row=13)

codes3 = ["Шифровать", "Дешифровать"]
# по умолчанию будет выбран первый элемент из codes
languages_var3 = tk.StringVar(value=codes3[0])

comboboxv1 = ttk.Combobox(textvariable=languages_var3, values=codes3, state="readonly")
comboboxv1.grid(column=1, row=13)

lblv2 = tk.Label(root, text="Введите текст:", font='Times 12', bg = "pink")
lblv2.grid(column=0, row=14)


messagev1 = tk.Text(width=60, height=4)
messagev1.grid(column=1, row=14)

scrollv1 = tk.Scrollbar(command=messagev1.yview)
scrollv1.grid(column=2, row=14)

messagev1.config(yscrollcommand=scrollv1.set)
tk.Button(root, text="Open File", command=openFile3).grid(column=0, row=15)

lblv3 = tk.Label(root, text="Введите ключ:", font='Times 12', bg = "pink")
lblv3.grid(column=0, row=16)

keyv2 = tk.Text(width=60, height=2)
keyv2.grid(column=1, row=16)

btnv4 = tk.Button(root, textvariable=languages_var3, command=clicked3)
btnv4.grid(column=0, row=17)

lblv4 = tk.Label(root, text="Вот ваш зашифрованный текст:", font='Times 12', bg = "pink")
lblv4.grid(column=0, row=18)

ans_Vernam = tk.Text(width=60, height=4)
ans_Vernam.grid(column=1, row=18)

scrollv5 = tk.Scrollbar(command=ans_Vernam.yview)
scrollv5.grid(column=2, row=18)

ans_Visioner.config(yscrollcommand=scrollv5.set)


root.mainloop()
