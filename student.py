from tkinter import *


def add_student():
    global student_screen
    student_screen = Toplevel(main_screen)
    student_screen.title("Add Bus Details")
    student_screen.geometry('512x512')


def main_page():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("512x512")
    main_screen.title('Student details')
    Label(text="Welcome to College Bus Fees Management", bg='white', width="512", height="2").pack()
    Label(text='').pack()
    Button(text='Add Student Details', height='2', width='30', command=add_student).pack()
    Label(text='').pack()
    Button(text='Display Student Details', height='2', width='30').pack()
    Label(text='').pack()

    main_screen.mainloop()


main_page()