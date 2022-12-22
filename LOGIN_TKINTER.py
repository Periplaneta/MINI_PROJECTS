import tkinter as tk
import os
from PIL import ImageTk, Image

root = tk.Tk()
root.resizable(width=False, height=False)
root.config()
root.geometry('500x500')

img = Image.open('./kisspng-web-development-mobile-app-development-software-de-5b09609b8ccb23.9599543815273412115767.png').convert('RGBA')
img= img.resize((500,300))
header_img = ImageTk.PhotoImage(img)
header = tk.Label(root,fg='red', image=header_img)
header.pack(fill='x')

login = tk.Label(root,font='montserrat 18 bold', text='LOGIN ENIMIL',bg='black',fg='white')
login.pack(pady=10)

frame1 = tk.Frame(root,height=100, highlightcolor='red')
frame1.pack()

uname = tk.Label(frame1, text='USER NAME', font='ARIAL 13 bold')
uname.grid(row=1, column=1)

entry_variable = tk.StringVar()
uname_ent = tk.Entry(frame1, textvariable=entry_variable, font='ARIAL 13 ')
uname_ent.grid(row=1, column=2, padx=3)

pas_variable = tk.StringVar()
password = tk.Label(frame1, text='PASSWORD', font='ARIAL 13 bold')
password.grid(row=2, column=1, pady=5)
password_ent = tk.Entry(frame1,show='*', textvariable=pas_variable, font='ARIAL 13 ')
password_ent.grid(row=2, column=2, padx=3, pady=5)


# creating the submit button
def submit():
    with open('test.txt', 'at') as file:
        file.write(f'{entry_variable}, {pas_variable}\n')

submit_button = tk.Button(root, text='SUBMIT', state='disabled', font='montserrat 14 bold', command= submit)
submit_button.pack(pady=15)

def check(*args):
    u = entry_variable.get()
    p = pas_variable.get()
    if u and p:
        submit_button.config(state='normal')
    else:
        submit_button.config(state='disabled')

entry_variable.trace('w', check)
pas_variable.trace('w', check)











tk.mainloop()