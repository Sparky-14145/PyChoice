'''
gui.py
Graphic User Interface support.
'''

import tkinter, connection, str_def, tkinter.font

win = tkinter.Tk()
win.title("PyChoice")
win.geometry("480x500")

ft1 = tkinter.font.Font(size=20)

text = tkinter.Text(win, width=30, height=10, font=ft1)
str = str_def.get_lang("hello")
text.insert(tkinter.INSERT, str)
text.grid(row=0, column=0, columnspan=4)
# text.pack(side=tkinter.LEFT)

scroll = tkinter.Scrollbar(win)
scroll.grid(row=0, column=5, rowspan=8, sticky=tkinter.N+tkinter.S)
# scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

button = tkinter.Button(win, text = str_def.get_lang("action"), font=ft1)
button.grid(row=2, column=0)
# button.pack(side=tkinter.BOTTOM, anchor=tkinter.W)

num_txt = tkinter.Variable()
entry = tkinter.Entry(win, textvariable=num_txt, font=tkinter.font.Font(size=30))
num_txt.set(str_def.get_lang("mount_init"))
entry.grid(row=1, column=0)
# entry.pack(side=tkinter.TOP)

def click():
    global str
    val = num_txt.get()
    if val.isdigit():
        str = connection.sample(int(val))
        text.delete("1.0", "end")
        for i in str:
            text.insert(tkinter.INSERT, i + '\n')
    else:
        text.replace("1.0", "end", str_def.get_lang("not_a_num"))

button.config(command=click)

tkinter.mainloop()