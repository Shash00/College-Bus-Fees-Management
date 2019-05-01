from tkinter import *
from tkinter import messagebox
import csv


def bus_add():
    global bus_number
    global num_entry
    global driver_name
    global name_entry
    global bus_screen
    bus_screen = Toplevel(main_screen)
    bus_screen.title("Add Bus Details")
    bus_screen.geometry('512x512')
    bus_number = StringVar()
    driver_name = StringVar()

    Label(bus_screen, text='Please enter bus details below').place(x=10, y=10)
    Label(bus_screen, text="").pack()
    Label(bus_screen, text='Bus number').place(x=10, y=60)
    num_entry = Entry(bus_screen, textvariable=bus_number).place(x=100, y=60)

    Label(bus_screen, text='Driver Name').place(x=10, y=100)
    name_entry = Entry(bus_screen, textvariable=driver_name).place(x=100, y=100)

    Button(bus_screen, text='Add', command=add_bus).place(relx=0.5, rely=0.7)


def add_bus():
    num_info = bus_number.get()
    name_info = driver_name.get()
    file = open('test.csv', 'a')
    file.write(num_info + ',')
    file.write(name_info + '\n')
    file.close()
    messagebox.showinfo('Success', "Details added successfully")


def bus_display():
    global display_bus
    display_bus = Toplevel(main_screen)
    display_bus.title("Add Bus Details")
    display_bus.geometry('512x512')
    Label(display_bus, text='Bus Number')
    with open("test.csv", newline="") as file:
        reader = csv.reader(file)

        # r and c tell us where to grid the labels
        r = 0
        for col in reader:
            c = 0
            for row in col:
                # i've added some styling
                Label(display_bus, width=10, height=2, text=row, relief=RIDGE).grid(row=r, column=c)
                c += 1
            r += 1


def main_page():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("512x512")
    main_screen.title('Details')
    Label(text="Welcome to College Bus Fees Management", bg='white', width="512", height="2").pack()
    Label(text='').pack()
    Button(text='Add Bus Details', height='2', width='30', command=bus_add).pack()
    Label(text='').pack()
    Button(text='Display Bus Details', height='2', width='30', command=bus_display).pack()
    Label(text='').pack()

    main_screen.mainloop()


main_page()
