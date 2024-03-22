from tkinter import *
import os.path

if not os.path.exists('passwords.txt'):
    f = open('passwords.txt', 'w')
    f.close()


def new_password():
    password_service_str = entry.get()
    entry.delete(0, END)
    try:
        password_service_list = password_service_str.split(':')
        service = password_service_list[0]
        password = password_service_list[1]
        f = open('passwords.txt', 'r')
        lines = f.read().split('\n')
        for line in lines:
            if service.lower() == line.split(':')[0]:
                label['text'] = 'You wrote password for this service!'
                return
        f = open('passwords.txt', 'a')
        f.write(f'{service.lower()}:{password}\n')
        f.close()
        label['text'] = 'Password was added!'
    except Exception:
        label['text'] = 'Error enter service and password!'


def get_password():
    service = entry.get()
    entry.delete(0, END)
    f = open('passwords.txt', 'r')
    lines = f.read().split('\n')
    for line in lines:
        if service.lower() == line.split(':')[0]:
            label['text'] = line.split(':')[1]
            return
    f.close()
    label['text'] = 'No this service!'


root = Tk()

root.geometry('310x400')
root.title('Password Manager')
root.config(background='red')
root.resizable(width=False, height=False)

get_btn = Button(root, text='Get Password', background='blue', font=('Avial', 13), command=get_password)
get_btn.pack(side=TOP)

write_btn = Button(root, text='New Password', background='blue', font=('Avial', 13), command=new_password)
write_btn.pack(side=TOP, pady=10)

entry = Entry(width=100, font=('Avial', 16))
entry.pack()

label = Label(text='', font=('Avial', 14), background='red')
label.pack()

root.mainloop()
