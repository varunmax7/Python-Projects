from tkinter import*
from tkinter import messagebox
window=Tk()
def Login_Function():
    email=Email_Input.get()
    password = Password_Input.get()
    if email=="varun@mgit.ac.in" and password == '12345':
        messagebox.showinfo('Congrats','Login Successful')
    else:
        messagebox.showerror('Error', 'Login Failed')
def Reset_Function():
    Email_Input.delete(0, 'end')
    Password_Input.delete(0, 'end')
window.title ('Login Window')
window.geometry('800x500')
window.configure(background='light blue')
Welcome_Label = Label(window, text="Welcome to MGIT Mail Services", fg='black', bg='light blue')
Welcome_Label.pack(pady=(30,30))
Welcome_Label.config(font=('verdana',30))
Email_Label = Label(window, text='Enter Email', fg='black', bg='light blue')
Email_Label.pack(pady=(20,10))
Email_Label.config(font=('verdana',20))
Email_Input = Entry(window, width = 60)
Email_Input.pack(ipady=10, pady=(3, 5))
Password_Label = Label(window, text='Enter Password', fg='black', bg='light blue')
Password_Label.pack(pady=(20,10))
Password_Label.config(font=('verdana',20))
Password_Input = Entry(window, width = 60)
Password_Input.pack(ipady=10, pady=(3, 5))
Submit_Button = Button(window, text='Submit', fg='yellow', bg='blue', width=10, height = 1, command=Login_Function)
Submit_Button.pack(ipadx=5, pady=(20,10))
Reset_Button = Button(window, text='Reset', fg='yellow', bg='blue', width=10, height = 1,command=Reset_Function)
Reset_Button.pack(ipadx=5, pady=(20,10))
window.mainloop()
