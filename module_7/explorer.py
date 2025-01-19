import tkinter
import os
from tkinter import filedialog
from tkinter.filedialog import askopenfile, askopenfilename


def file_select():
    filename = askopenfilename(initialdir=".", title="Выберите файл",
                               filetypes=(('Текстовый файл', '.txt'),
                                          ('Все файлы','*')))
    text['text'] = text['text'] + ' ' + filename
    os.startfile(filename)

window = tkinter.Tk()
window.title('Проводник')
window.geometry('450x150')
window.configure(bg='black')
window.resizable(False,False)
text = tkinter.Label(window, text='Файл:', width=65, height=5, background='silver', foreground='blue')
text.grid(column=1, row=1)
button_select = tkinter.Button(window, width=20, height=3, text='Выбрать файл',
                               background='silver', foreground='blue',
                               command=file_select)
button_select.grid(column=1, row=2, pady = 5)
window.mainloop()
