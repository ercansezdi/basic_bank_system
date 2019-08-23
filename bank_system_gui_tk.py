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

    def add_activities(self,money,user,operation,transfer_user):

        if operation == "deposit":
            self.activities[user][0] = self.activities[user][0] + int(money)
            self.activities[user][1].append(
                "deposid " + str(money) + " " + datetime.today().strftime('%d-%m-%y  %H:%M:%S'))
        elif operation == "withdraw":
            self.activities[user][0] = self.activities[user][0] - int(money)
            self.activities[user][1].append(
                "withdrawed " + str(money) + " " + datetime.today().strftime('%d-%m-%y  %H:%M:%S'))
        elif operation == "transfer":
            self.activities[user][0] = self.activities[user][0] - int(money)
            self.activities[user][1].append("Transferred " + str(money) + " " + datetime.today().strftime('%d-%m-%y  %H:%M:%S'))
            self.activities[transfer_user][0] = self.activities[transfer_user][0] + int(money)
            self.activities[transfer_user][1].append("Transferred to me from " +transfer_user + " " +str(money) + " " + datetime.today().strftime('%d-%m-%y  %H:%M:%S'))



class basic_bank_system_gui(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.parent.geometry('600x600')
        # Frames
        self.loginPage = Frame(self.parent)
        self.userLoginPage = Frame(self.parent)
        self.loginUser = Frame(self.parent)
        self.userOperations = Frame(self.parent)


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
        button1 = Button(self.loginUser,text = "Withdraw Money",wraplength=750,anchor="center",height=1,width=13,command=lambda: self.user_operations("withdraw"))
        button1.grid(row=0,column=0)
        button2 = Button(self.loginUser,text = "Deposit Money",wraplength=750,anchor="center",height=1,width=13,command=lambda: self.user_operations("deposit"))
        button2.grid(row=1,column=0)
        button3 = Button(self.loginUser,text = "Transfer Money",wraplength=750,anchor="center",height=1,width=13,command=lambda: self.user_operations("tranfer_money"))
        button3.grid(row=2,column=0)
        button4 = Button(self.loginUser,text = "My Account Information",wraplength=750,anchor="center",height=1,width=13,command=lambda: self.user_operations("info"))
        button4.grid(row=3,column=0)
        button5 = Button(self.loginUser,text = "Logout",wraplength=750,anchor="center",height=1,width=13,command=lambda:[self.loginUser.grid_remove(),self.login_page()])
        button5.grid(row=4,column=0)
    def user_operations(self,process):
        self.userOperations.grid(row=0,column=0)
        self.loginUser.grid_remove()

        if process == "withdraw":
            withdrawLabel = Label(self.userOperations,text="How much do you wish to withdraw ",justify = LEFT,font ="Helvetica 15 bold italic")
            withdrawLabel.grid(row=0,column=0)
            withdrawEntry =  Entry(self.userLoginPage,font ="Helvetica 12 bold italic")
            withdrawEntry.grid(row=1,column=0)
            withdrawButton = Button(self.loginUser,text = "Withdraw Money",wraplength=750,anchor="center",height=1,width=13,command=lambda: self.operation_control("withdraw",withdrawEntry.get(),"empty"))
            withdrawButton.grid(row=2,column=0)
        elif process == "deposit":
            depositLabel = Label(self.userOperations,text="How much do you wish to deposite",justify = LEFT,font ="Helvetica 15 bold italic")
            depositLabel.grid(row=0,column=0)
            depositEntry =  Entry(self.userOperations,font ="Helvetica 12 bold italic")
            depositEntry.grid(row=1,column=0)
            depositButton = Button(self.userOperations,text = "Deposit Money",wraplength=750,anchor="center",height=1,width=13,command=lambda: self.operation_control("deposit",depositEntry.get(),"empty"))
            depositButton.grid(row=2,column=0)
        elif  process == "tranfer_money":
            pass
        else:
            pass
    def operation_control(self,operation,money,transfer_user):
        if operation == "withdraw":
            if int(money) > 0:
                pass
            else:
                messagebox.showinfo("Warning",  "Not enough balance")
        elif operation == "deposit":
            if int(money) > 0:
                self.data.add_activities(money,self.usernameLoginEntry.get(),operation,transfer_user)
                string = "Deposit " + money + " TL." ;
                messagebox.showinfo("Warning", string)
                self.userOperations.grid_remove()
                self.login_user()
            else:
                messagebox.showinfo("Warning", "Wrong money entry")

        elif operation == "tranfer_money":
            pass
        else:
            pass





if __name__ == "__main__":
    root = Tk()
    root.call('tk', 'scaling', 1.0)
    run = basic_bank_system_gui(root)
    root.mainloop()
