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
                "deposid " + str(money) + " TL " + datetime.today().strftime('%d-%m-%y  %H:%M:%S'))
        elif operation == "withdraw":
            self.activities[user][0] = self.activities[user][0] - int(money)
            self.activities[user][1].append(
                "withdrawed " + str(money) + " TL " + datetime.today().strftime('%d-%m-%y  %H:%M:%S'))
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
        self.defines()


        #Classes
        self.data = datas()


        self.login_page()
    def login_page(self):
        self.loginPage.grid(row=0,column=0)
        self.text_1.grid(row=0,column=2,rowspan = 2,columnspan=3)
        self.text_2.grid(row=2,column=2,rowspan=2,columnspan=3)
        self.buttonUser.grid(row=4,column=2,rowspan=2,columnspan=3)
        self.button_login_exit.grid(row=6,column=2,rowspan=2,columnspan=3)

    def user_login_page(self):
        self.loginPage.grid_remove()
        self.userLoginPage.grid(row=0,column=0)
        self.loginUsername.grid(row=0,column=0)
        self.usernameLoginEntry.grid(row=1,column=0)
        self.loginPassword.grid(row=2,column=0)
        self.passwordLoginEntry.grid(row=3,column=0)
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
        self.button1.grid(row=0,column=0)
        self.button2.grid(row=1,column=0)
        self.button3.grid(row=2,column=0)
        self.button4.grid(row=3,column=0)
        self.button5.grid(row=4,column=0)

    def defines(self):
        #login_page
        self.text_1 = Label(self.loginPage,text = "Basic Bank System v.01 ",justify = LEFT,font ="Helvetica 15 bold italic")
        self.text_2 = Label(self.loginPage,text = " Mersin, Turkey " + datetime.today().strftime('%d-%m-%y  %H:%M:%S'),justify = LEFT,font ="Helvetica 15 bold italic")
        self.buttonUser = Button(self.loginPage,text = "Login",wraplength=750,anchor="center",height=1,width=13,command=self.user_login_page)
        self.button_login_exit = Button(self.loginPage,text = "Exit",wraplength=750,anchor="center",height=1,width=13,command = self.parent.destroy)
        #user_login_page
        self.loginUsername = Label(self.userLoginPage,text="Enter your username",justify = LEFT,font ="Helvetica 15 bold italic")
        self.usernameLoginEntry = Entry(self.userLoginPage,font ="Helvetica 12 bold italic")
        self.loginPassword = Label(self.userLoginPage,text="Enter your password",justify = LEFT,font ="Helvetica 15 bold italic")
        self.passwordLoginEntry = Entry(self.userLoginPage,font ="Helvetica 12 bold italic")
        self.button_user = Button(self.userLoginPage,text = "Login",wraplength=750,anchor="center",height=1,width=13,command=self.checking_data)

        #login_user
        self.button1 = Button(self.loginUser,text = "Withdraw Money",wraplength=750,anchor="center",height=1,width=13,command=lambda: self.user_operations("withdraw"))
        self.button2 = Button(self.loginUser,text = "Deposit Money",wraplength=750,anchor="center",height=1,width=13,command=lambda: self.user_operations("deposit"))
        self.button3 = Button(self.loginUser,text = "Transfer Money",wraplength=750,anchor="center",height=1,width=13,command=lambda: self.user_operations("tranfer_money"))
        self.button4 = Button(self.loginUser,text = "My Account Information",wraplength=750,anchor="center",height=1,width=13,command=lambda: self.user_operations("info"))
        self.button5 = Button(self.loginUser,text = "Logout",wraplength=750,anchor="center",height=1,width=13,command=lambda:[self.loginUser.grid_remove(),self.login_page()])

        #user_operations
        self.withdrawLabel = Label(self.userOperations,text="How much do you wish to withdraw ",justify = LEFT,font ="Helvetica 15 bold italic")
        self.withdrawEntry =  Entry(self.userOperations,font ="Helvetica 12 bold italic")
        self.withdrawButton = Button(self.userOperations,text = "Withdraw Money",wraplength=750,anchor="center",height=1,width=13,command=lambda:[self.operation_control("withdraw",self.withdrawEntry.get(),False),self.withdrawEntry.delete(0, 'end')])
        self.withdrawExit = Button(self.userOperations,text = "Close Panel",wraplength=750,anchor="center",height=1,width=13,command=lambda:[self.userOperations.grid_remove(),self.withdrawEntry.delete(0, 'end'),self.login_user()])
        self.depositLabel = Label(self.userOperations,text="How much do you wish to deposite",justify = LEFT,font ="Helvetica 15 bold italic")
        self.depositEntry =  Entry(self.userOperations,font ="Helvetica 12 bold italic")
        self.depositButton = Button(self.userOperations,text = "Deposit Money",wraplength=750,anchor="center",height=1,width=13,command=lambda:[ self.operation_control("deposit",self.depositEntry.get(),False),self.depositEntry.delete(0, 'end')])
        self.depositExit = Button(self.userOperations,text = "Close Panel",wraplength=750,anchor="center",height=1,width=13,command=lambda:[self.userOperations.grid_remove(),self.depositEntry.delete(0, 'end'),self.login_user()])
        self.transferLabel_1 = Label(self.userOperations,text="For who do you wish to transfer to",justify = LEFT,font ="Helvetica 15 bold italic")
        self.transferEntry_1 =  Entry(self.userOperations,font ="Helvetica 12 bold italic")
        self.transferLabel_2 = Label(self.userOperations,text="How much would like to transfer",justify = LEFT,font ="Helvetica 15 bold italic")
        self.transferEntry_2 =  Entry(self.userOperations,font ="Helvetica 12 bold italic")
        self.transferButton = Button(self.userOperations,text = "Transfer Money",wraplength=750,anchor="center",height=1,width=13,command=lambda:[ self.operation_control("transfer_money",self.transferEntry_2.get(),self.transferEntry_1.get()),self.transferEntry_1.delete(0, 'end'),self.transferEntry_2.delete(0, 'end')])
        self.transferExit = Button(self.userOperations,text = "Close Panel",wraplength=750,anchor="center",height=1,width=13,command=lambda:[self.userOperations.grid_remove(),self.transferEntry_1.delete(0, 'end'),self.transferEntry_2.delete(0, 'end'),self.login_user()])
    def user_operations(self,process):
        self.userOperations.grid(row=0,column=0)
        self.loginUser.grid_remove()

        self.withdrawLabel.grid_remove()
        self.withdrawEntry.grid_remove()
        self.withdrawButton.grid_remove()
        self.withdrawExit.grid_remove()
        self.depositLabel.grid_remove()
        self.depositEntry.grid_remove()
        self.depositButton.grid_remove()
        self.depositExit.grid_remove()
        self.transferLabel_1.grid_remove()
        self.transferEntry_1.grid_remove()
        self.transferLabel_2.grid_remove()
        self.transferEntry_2.grid_remove()
        self.transferButton.grid_remove()
        self.transferExit.grid_remove()

        if process == "withdraw":
            self.withdrawLabel.grid(row=0,column=0)
            self.withdrawEntry.grid(row=1,column=0)
            self.withdrawButton.grid(row=4,column=0)
            self.withdrawExit.grid(row=5,column=0)
        elif process == "deposit":
            self.depositLabel.grid(row=0,column=0)
            self.depositEntry.grid(row=1,column=0)
            self.depositButton.grid(row=2,column=0)
            self.depositExit.grid(row=3,column=0)
        elif  process == "tranfer_money":
            self.transferLabel_1.grid(row=0,column=0)
            self.transferEntry_1.grid(row=1,column=0)
            self.transferLabel_2.grid(row=2,column=0)
            self.transferEntry_2.grid(row=3,column=0)
            self.transferButton.grid(row=4,column=0)
            self.transferExit.grid(row=5,column=0)
        else:
            self.operation_control("info",False,False)

    def operation_control(self,operation,money,transfer_user):
        if operation == "withdraw":

            if int(money) > 0:
                data1 ,data2 = self.data.request_data()
                for i in data1:
                    if i == self.usernameLoginEntry.get():
                        balance = data1[i][0]
                if int(money) < balance:
                    self.data.add_activities(money,self.usernameLoginEntry.get(),operation,transfer_user)
                    string = "Withdraw " + money + " TL." ;
                    messagebox.showinfo("Warning", string)
                    self.userOperations.grid_remove()
                    self.login_user()
                else:
                    messagebox.showinfo("Warning",  "Not enough balance")
            else:
                messagebox.showinfo("Warning",  "Wrong money input")
        elif operation == "deposit":
            if money == "":
                messagebox.showinfo("Warning", "Wrong money entry")
            else:
                if int(money) > 0:
                    self.data.add_activities(money,self.usernameLoginEntry.get(),operation,transfer_user)
                    string = "Deposit " + money + " TL." ;
                    messagebox.showinfo("Warning", string)
                    self.userOperations.grid_remove()
                    self.login_user()


                else:
                    messagebox.showinfo("Warning", "Wrong money entry")


        elif operation == "transfer_money":
            activities ,users = self.data.request_data()
            control = False
            for i in users:
                if(i == transfer_user):
                    control = True
            if control:
                if money == "":
                    messagebox.showinfo("Warning", "Wrong money entry")
                else:
                    if int(money) > 0:
                        for i in activities:
                            if i == self.usernameLoginEntry.get():
                                if activities[i][0] > int(money):
                                    self.data.add_activities(int(money),self.usernameLoginEntry.get(),"transfer",transfer_user)
                                    messagebox.showinfo("Warning","Transferring " + money + "TL to " + transfer_user + "Succeeded.")
                                    self.userOperations.grid_remove()
                                    self.login_user()
                                else:
                                    messagebox.showinfo("Warning", "Not enough balance")
                            else:
                                pass
                    else:
                        messagebox.showinfo("Warning", "Wrong money entry")
            else:
                messagebox.showinfo("Warning", "Not found transfer user")


        else: #show user information
            self.userOperations.grid_remove()
            showInfo = Frame(self.parent)
            showInfo.grid(row=0,column=0)
            textInfo = Text(showInfo)
            textInfo.grid(row=0,column=0)

            data1 ,data2 = self.data.request_data()
            textInfo.insert(INSERT,"| __________________________ User Data __________________________ |\n")
            for name in data1:
                if (name == self.usernameLoginEntry.get()):
                    textInfo.insert(INSERT,"Date: " + datetime.today().strftime('%d-%m-%y'))
                    textInfo.insert(INSERT,"\n")
                    textInfo.insert(INSERT,("Time: " + datetime.today().strftime('%H:%M:%S')))
                    textInfo.insert(INSERT,"\n")
                    textInfo.insert(INSERT,"Your: " + name)
                    textInfo.insert(INSERT,"\n")
                    textInfo.insert(INSERT,"Password: " + data2[name])
                    textInfo.insert(INSERT,"\n")
                    textInfo.insert(INSERT,"Balance : " + str(data1[name][0]))
                    textInfo.insert(INSERT,"\n")

            textInfo.insert(INSERT,"| _________________________ Transactions _________________________ |\n")
            for i in data1:
                if (i == self.usernameLoginEntry.get()):
                    for message in data1[i][1]:
                        message  = message + "\n"
                        textInfo.insert(INSERT,message)
                        textInfo.insert(INSERT,"\n")
            textInfo.insert(END,"\n")

            textButton = Button(showInfo,text= "Exit",wraplength=750,anchor="center",height=1,width=13,command=lambda:[showInfo.destroy(),self.login_user()])
            textButton.grid(row=1,column=0)





if __name__ == "__main__":
    root = Tk()
    root.call('tk', 'scaling', 1.0)
    run = basic_bank_system_gui(root)
    root.mainloop()
