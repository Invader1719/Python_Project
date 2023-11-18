import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from Chiper_Coder import chipper
from Chiper_Coder import chipper_hack
from Visioner_Coder import visioner
from Visioner_Coder import devisioner
from Vernam import vernam_coder

class Screen():

    def openFile(self):
        self.tf = filedialog.askopenfilename(
            initialdir="C:/Users/MainFrame/Desktop/",
            title="Open Text file",
            filetypes=(("Text Files", "*.txt"),)
        )
        self.tf = open(self.tf, 'r')
        self.data = self.tf.read()
        self.message.insert(tk.END, self.data)
        self.tf.close()

    def openFile2(self):
        self.tf = filedialog.askopenfilename(
            initialdir="C:/Users/MainFrame/Desktop/",
            title="Open Text file",
            filetypes=(("Text Files", "*.txt"),)
        )
        tf = open(self.tf, 'r')
        self.data = tf.read()
        self.message4.insert(tk.END, self.data)
        self.tf.close()

    def openFile3(self):
        self.tf = filedialog.askopenfilename(
            initialdir="C:/Users/MainFrame/Desktop/",
            title="Open Text file",
            filetypes=(("Text Files", "*.txt"),)
        )
        self.tf = open(self.tf, 'r')
        self.data = self.tf.read()
        self.messagev1.insert(tk.END, self.data)
        self.tf.close()

    def clicked(self):
        s = self.message.get(1.0, tk.END)
        k = self.key.get(1.0, tk.END)
        if self.languages_var.get() == "Шифровать":
            otv = chipper(s, k)
        elif self.languages_var.get() == "Взломать!":
            otv = chipper_hack(s)
        else:
            otv = chipper(s, "-" + k)

        self.ans.delete(1.0, tk.END)
        self.ans.insert(1.0, otv)

    def clicked2(self):
        s = self.message4.get(1.0, tk.END)
        k = self.key4.get(1.0, tk.END)
        if self.languages_var2.get() == "Шифровать":
            otv = visioner(s, k)
        else:
            otv = devisioner(s, k)
        self.ans_Visioner.delete(1.0, tk.END)
        self.ans_Visioner.insert(1.0, otv)

    def clicked3(self):
        s = self.messagev1.get(1.0, tk.END)
        k = self.keyv2.get(1.0, tk.END)
        otv = vernam_coder(s, k)
        self.ans_Vernam.delete(1.0, tk.END)
        self.ans_Vernam.insert(1.0, otv)

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("coder")
        self.root.geometry("1500x800")
        self.root.configure(bg='pink')
        self.bg = tk.PhotoImage(file="Rayan_Gosling.png")
        self.label1 = tk.Label(self.root, image=self.bg)
        self.label1.place(x=0, y=0)

        self.chiper_intro = tk.Label(self.root, text="Тут Шифр Цезаря. Я хочу:", font='Times 12', bg="pink")
        self.chiper_intro.grid(column=0, row=0)

        codes = ["Шифровать", "Дешифровать", "Взломать!"]  # tk.Button
        # по умолчанию будет выбран первый элемент из codes
        self.languages_var = tk.StringVar(value=codes[0])

        self.combobox = ttk.Combobox(textvariable=self.languages_var, values=codes, state="readonly")
        self.combobox.grid(column=1, row=0)

        self.lbl = tk.Label(self.root, text="Введите текст:", font='Times 12', bg="pink")
        self.lbl.grid(column=0, row=1)

        self.message = tk.Text(width=60, height=4)
        self.message.grid(column=1, row=1)

        self.scroll = tk.Scrollbar(command=self.message.yview)
        self.scroll.grid(column=2, row=1)

        self.message.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.message.yview)

        tk.Button(self.root, text="Open File", command=self.openFile).grid(column=0, row=3)

        self.lbl2 = tk.Label(self.root, text="Введите ключ:", font='Times 12', bg="pink")
        self.lbl2.grid(column=0, row=4)

        self.key = tk.Text(width=60, height=2)
        self.key.grid(column=1, row=4)

        self.btn = tk.Button(self.root, textvariable = self.languages_var, command=self.clicked)
        self.btn.grid(column=0, row=5)

        self.lbl3 = tk.Label(self.root, text="Вот ваш зашифрованный текст:", font='Times 12', bg="pink")
        self.lbl3.grid(column=0, row=6)

        self.ans = tk.Text(width=60, height=4)
        self.ans.grid(column=1, row=6)

        self.scroll2 = tk.Scrollbar(command=self.ans.yview)
        self.scroll2.grid(column=2, row=6)

        self.ans.config(yscrollcommand = self.scroll2.set)

        self.lbl7 = tk.Label(self.root, text="Тут шифр Виженера. Я хочу:", font='Times 12', bg="pink")
        self.lbl7.grid(column=0, row=7)

        self.codes2 = ["Шифровать", "Дешифровать"]
        # по умолчанию будет выбран первый элемент из codes
        self.languages_var2 = tk.StringVar(value=self.codes2[0])

        self.combobox2 = ttk.Combobox(textvariable=self.languages_var2, values=self.codes2, state="readonly")
        self.combobox2.grid(column=1, row=7)

        self.lbl8 = tk.Label(self.root, text="Введите текст:", font='Times 12', bg="pink")
        self.lbl8.grid(column=0, row=8)

        self.message4 = tk.Text(width=60, height=4)
        self.message4.grid(column=1, row=8)

        self.scroll3 = tk.Scrollbar(command=self.message.yview)
        self.scroll3.grid(column=2, row=8)

        self.message4.config(yscrollcommand=self.scroll3.set)
        tk.Button(self.root, text="Open File", command=self.openFile2).grid(column=0, row=9)

        self.lbl9 = tk.Label(self.root, text="Введите ключ:", font='Times 12', bg="pink")
        self.lbl9.grid(column=0, row=10)

        self.key4 = tk.Text(width=60, height=2)
        self.key4.grid(column=1, row=10)

        self.btn4 = tk.Button(self.root, textvariable=self.languages_var2, command=self.clicked2)
        self.btn4.grid(column=0, row=11)

        self.lbl10 = tk.Label(self.root, text="Вот ваш зашифрованный текст:", font='Times 12', bg="pink")
        self.lbl10.grid(column=0, row=12)

        self.ans_Visioner = tk.Text(width=60, height=4)
        self.ans_Visioner.grid(column=1, row=12)

        self.scroll4 = tk.Scrollbar(command=self.message.yview)
        self.scroll4.grid(column=2, row=12)

        self.ans_Visioner.config(yscrollcommand=self.scroll4.set)

        self.lblv1 = tk.Label(self.root, text="Тут шифр Вернама. Я хочу:", font='Times 12', bg="pink")
        self.lblv1.grid(column=0, row=13)

        self.codes3 = ["Шифровать", "Дешифровать"]
        # по умолчанию будет выбран первый элемент из codes
        self.languages_var3 = tk.StringVar(value=self.codes3[0])

        self.comboboxv1 = ttk.Combobox(textvariable=self.languages_var3, values=self.codes3, state="readonly")
        self.comboboxv1.grid(column=1, row=13)

        self.lblv2 = tk.Label(self.root, text="Введите текст:", font='Times 12', bg="pink")
        self.lblv2.grid(column=0, row=14)

        self.messagev1 = tk.Text(width=60, height=4)
        self.messagev1.grid(column=1, row=14)

        self.scrollv1 = tk.Scrollbar(command=self.messagev1.yview)
        self.scrollv1.grid(column=2, row=14)

        self.messagev1.config(yscrollcommand=self.scrollv1.set)
        tk.Button(self.root, text="Open File", command=self.openFile3).grid(column=0, row=15)

        self.lblv3 = tk.Label(self.root, text="Введите ключ:", font='Times 12', bg="pink")
        self.lblv3.grid(column=0, row=16)

        self.keyv2 = tk.Text(width=60, height=2)
        self.keyv2.grid(column=1, row=16)

        self.btnv4 = tk.Button(self.root, textvariable=self.languages_var3, command=self.clicked3)
        self.btnv4.grid(column=0, row=17)

        self.lblv4 = tk.Label(self.root, text="Вот ваш зашифрованный текст:", font='Times 12', bg="pink")
        self.lblv4.grid(column=0, row=18)

        self.ans_Vernam = tk.Text(width=60, height=4)
        self.ans_Vernam.grid(column=1, row=18)

        self.scrollv5 = tk.Scrollbar(command=self.ans_Vernam.yview)
        self.scrollv5.grid(column=2, row=18)

        self.ans_Visioner.config(yscrollcommand=self.scrollv5.set)

    def Mainlooop(self):
        self.root.mainloop()
