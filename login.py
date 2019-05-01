from tkinter import *


def login():
    global login_screen
    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry

    login_screen = Toplevel(main_screen)
    login_screen.title('Login')
    login_screen.geometry('512x512')
    Label(login_screen, text='Please Enter details below to login').pack()
    Label(login_screen, text="").pack()

    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text='Username').pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text='').pack()
    Label(login_screen, text='Password').pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text='').pack()
    Button(login_screen, text='Login', width=10, height=1, command=login_verify).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    for line in open("users.txt", "r").readlines():  # Read the lines
        login_info = line.split()  # Split on the space, and store the results in a list of two strings
        if username1 == login_info[0] and password1 == login_info[1]:
            login_success()
            return TRUE
    password_not_recognised()


def login_success():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title('Login Success')
    login_success_screen.geometry('312x312')
    Label(login_success_screen, text='Login Success').pack()
    Button(login_success_screen, text='OK', command=delete_login_success).pack()


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title('Invalid Password')
    password_not_recog_screen.geometry('312x312')
    Label(password_not_recog_screen, text='Invalid Password').pack()
    Button(password_not_recog_screen, text='OK', command=delete_password_not_recognised).pack()


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title('User not found')
    user_not_found_screen.geometry('212x212')
    Label(user_not_found_screen, text='User not found').pack()
    Button(user_not_found_screen, text='OK', command=delete_user_not_found).pack()


def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found():
    user_not_found_screen.destroy()


def main_page():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("512x512")
    main_screen.title('Account Login')
    Label(text="Welcome to College Bus Fees Management", bg='white', width="512", height="2").pack()
    Label(text='').pack()
    Button(text='Login', height='2', width='30', command=login).pack()
    Label(text='').pack()

    main_screen.mainloop()


main_page()
