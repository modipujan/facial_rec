from tkinter import *
from tkinter.ttk import *
import shutil
from tkinter.filedialog import askopenfile



f = open("stu_details.txt", "r")
x = f.read()

def removeall():
    f = open("stu_details.txt", "r+")
    f.truncate(0)

fname = x

ws = Tk()
ws.title('Image')
ws.geometry('400x200')


def open_file():
    file_path = askopenfile(mode='r', filetypes=[('Image Files', '*jpeg')])
    if file_path is not None:
        print(file_path.name[-10])
        original = file_path.name
        target = r'pictures\{name}.jpeg'.format(name=fname)
        shutil.copyfile(original,target)
        removeall()
        pass
    ws.destroy()


adhar = Label(
    ws,
    text='Find the needed image '
)
adhar.grid(row=0, column=0, padx=10)

adharbtn = Button(
    ws,
    text='Choose File',
    command=lambda: open_file()
)
adharbtn.grid(row=0, column=1)
