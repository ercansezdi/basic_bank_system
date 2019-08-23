#!/usr/bin/env python
# -*- coding: utf8 -*-
from tkinter import messagebox
from tkinter import *

from datetime import datetime
from time import strftime

class datas:
    def __init__(self):
        self.activities = {"user_1": [0, []], "user_2": [ 0, []]}
        self.members = {"user_1": "1234", "user_2": "4321"}

    def request_data(self):
        return self.activities,self.members

class basic_bank_system_gui(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.parent.geometry('600x600')
        # Frames
        self.loginPage = Frame(self.parent)
        self.userLoginPage = Frame(self.parent)
        self.loginUser = Frame(self.parent)


        #Classes
        self.data = datas()



        self.login_page()
    def login_page(self):
        self.loginPage.grid(row=0,column=0)
        self.text_1 = Label(self.loginPage,text = "Basic Bank System v.01 ",justify = LEFT,font ="Helvetica 15 bold italic")
        self.text_1.grid(row=0,column=2,rowspan = 2,columnspan=3)
        self.text_2 = Label(self.loginPage,text = " Mersin, Turkey " + datetime.today().strftime('%d-%m-%y  %H:%M:%S'),justify = LEFT,font ="Helvetica 15 bold italic")
        self.text_2.grid(row=2,column=2,rowspan=2,columnspan=3)
        self.button_user = Button(self.loginPage,text = "Login",wraplength=750,anchor="center",height=1,width=13,command=self.user_login_page)
        self.button_user.grid(row=4,column=2,rowspan=2,columnspan=3)
        self.button_login_exit = Button(self.loginPage,text = "Exit",wraplength=750,anchor="center",height=1,width=13,command = self.parent.destroy)
        self.button_login_exit.grid(row=6,column=2,rowspan=2,columnspan=3)

    def user_login_page(self):
        self.loginPage.grid_remove()
        self.userLoginPage.grid(row=0,column=0)
        self.loginUsername = Label(self.userLoginPage,text="Enter your username",justify = LEFT,font ="Helvetica 15 bold italic")
        self.loginUsername.grid(row=0,column=0)
        self.usernameLoginEntry = Entry(self.userLoginPage,font ="Helvetica 12 bold italic")
        self.usernameLoginEntry.grid(row=1,column=0)
        self.loginPassword = Label(self.userLoginPage,text="Enter your password",justify = LEFT,font ="Helvetica 15 bold italic")
        self.loginPassword.grid(row=2,column=0)
        self.passwordLoginEntry = Entry(self.userLoginPage,font ="Helvetica 12 bold italic")
        self.passwordLoginEntry.grid(row=3,column=0)
        self.button_user = Button(self.userLoginPage,text = "Login",wraplength=750,anchor="center",height=1,width=13,command=self.checking_data)
        self.button_user.grid(row=4,column=0)

    def checking_data(self):
        username = self.usernameLoginEntry.get()
        password = self.passwordLoginEntry.get()
        activities,members = self.data.request_data()
        if username in members:
            if members[username] == password:
                self.login_user()
            else:
                messagebox.showinfo("Warning", "Username or password incorrect.")
        else:
            messagebox.showinfo("Warning", "Username or password incorrect.")

    def login_user(self):
        self.userLoginPage.grid_remove()
        self.loginUser.grid(row=0,column=0)
        button1 = Button(self.loginUser,text = "Withdraw Money",wraplength=750,anchor="center",height=1,width=13,command=lambda: self.withdraw_deposit_money("deposit"))
        button1.grid(row=0,column=0)
        button2 = Button(self.loginUser,text = "Deposit Money",wraplength=750,anchor="center",height=1,width=13,command=self.checking_data)
        button2.grid(row=1,column=0)
        button3 = Button(self.loginUser,text = "Transfer Money",wraplength=750,anchor="center",height=1,width=13,command=self.checking_data)
        button3.grid(row=2,column=0)
        button4 = Button(self.loginUser,text = "My Account Information",wraplength=750,anchor="center",height=1,width=13,command=self.checking_data)
        button4.grid(row=3,column=0)
        button5 = Button(self.loginUser,text = "Logout",wraplength=750,anchor="center",height=1,width=13,command=lambda:[self.loginUser.grid_remove(),self.login_page()])
        button5.grid(row=4,column=0)
    def withdraw_deposit_money(self,process):
        if process == "withdraw":
            pass
        elif process == "deposit":
            print('xxxx')
        else:
            pass






if __name__ == "__main__":
    root = Tk()
    root.call('tk', 'scaling', 1.0)
    run = basic_bank_system_gui(root)
    root.mainloop()
