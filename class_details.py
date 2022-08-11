from tkinter import *
import sqlite3


def option():
    from options import opt_win
    opt_win.mainloop()


top_win = Tk()
top_win.geometry('600x500')
top_win.title("Registration Form")

class_id = int()
class_name = StringVar()
batch_name = StringVar()


def database():
    c_id = entry_1.get()
    c_name = entry_2.get()
    b_name = entry_3.get()
    conn = sqlite3.connect('Form.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Class (CLASSID  INTEGER,CLASSNAME TEXT,BATCHNAME TEXT)')
    cursor.execute('INSERT INTO Class (CLASSID,CLASSNAME,BATCHNAME) VALUES(?,?,?)',
                   (c_id, c_name, b_name,))
    conn.commit()
    top_win.destroy()
    option()


# label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
# label_0.grid(row=0,column=0)

label_1 = Label(top_win, text="class id", width=20, font=("bold", 10))
label_1.place(x=20, y=40)

entry_1 = Entry(top_win, textvar=class_id)
entry_1.place(x=200, y=40)

label_2 = Label(top_win, text="class_name", width=20, font=("bold", 10))
label_2.place(x=20, y=70)

entry_2 = Entry(top_win, textvar=class_name)
entry_2.place(x=200, y=70)

label_3 = Label(top_win, text="batch_name", width=20, font=("bold", 10))
label_3.place(x=20, y=100)

entry_3 = Entry(top_win, textvar=batch_name)
entry_3.place(x=200, y=100)

Button(top_win, text='Submit', width=20, bg='brown', fg='white', command=database).place(x=180, y=380)

top_win.mainloop()
