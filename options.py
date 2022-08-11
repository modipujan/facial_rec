from tkinter import *
from markAttendance import *

opt_win = Tk()
opt_win.geometry('600x500')
opt_win.title("Options Form")

def func_call_student_details():
    opt_win.withdraw()
    from studentdetails import top_win
    top_win.mainloop()


def func_call_class_details():
    opt_win.withdraw()
    from class_details import top_win
    top_win.mainloop()


def trigger_attendance():
    MarkAttObj.takeAtt()
    print('w')

Button(opt_win, text='Add Student', width=20, bg='brown', fg='white', command=func_call_student_details).place(x=200, y=180)

Button(opt_win, text='Add class', width=20, bg='brown', fg='white', command=func_call_class_details).place(x=200, y=280)

Button(opt_win, text='Trigger Attendance', width=20, bg='brown', fg='white', command=trigger_attendance).place(x=200, y=380)

