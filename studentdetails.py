from tkinter import *
import sqlite3

top_win = Tk()
top_win.geometry('600x500')
top_win.title("Registration Form")





Fullname = StringVar()
firstname = StringVar()
lastname = StringVar()
classid = StringVar()
studentid = StringVar()

var1 = IntVar()

img_nam = StringVar()


def database():
    global s_id,f_name
    s_id = entry_1.get()
    f_name = entry_2.get()
    l_name = entry_3.get()
    class_id = entry_4.get()
    conn = sqlite3.connect('Form.db')

    f = open("stu_details.txt", "a")
    f.write(f_name+"."+s_id)
    f.close()

    with conn:
        cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Student (STUDENTID  INTEGER,FIRST_NAME TEXT,LAST_NAME TEXT,CLASS_ID TEXT)')
    cursor.execute('INSERT INTO Student (STUDENTID,FIRST_NAME,LAST_NAME,CLASS_ID) VALUES(?,?,?,?)',
                   (s_id, f_name, l_name, class_id))
    conn.commit()
    from image import ws
    ws.mainloop()
    return (s_id,f_name)




# label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
# label_0.grid(row=0,column=0)

label_1 = Label(top_win, text="Student id", width=20, font=("bold", 10))
label_1.place(x=20, y=40)

entry_1 = Entry(top_win, textvar=studentid)
entry_1.place(x=200, y=40)

label_2 = Label(top_win, text="FirstName", width=20, font=("bold", 10))
label_2.place(x=20, y=70)

entry_2 = Entry(top_win, textvar=firstname)
entry_2.place(x=200, y=70)

label_3 = Label(top_win, text="LastName", width=20, font=("bold", 10))
label_3.place(x=20, y=100)

entry_3 = Entry(top_win, textvar=lastname)
entry_3.place(x=200, y=100)

label_4 = Label(top_win, text="Class ID", width=20, font=("bold", 10))
label_4.place(x=20, y=130)

entry_4 = Entry(top_win, textvar=classid)
entry_4.place(x=200, y=130)

Button(top_win, text='Submit', width=20, bg='brown', fg='white', command=database).place(x=180, y=380)
