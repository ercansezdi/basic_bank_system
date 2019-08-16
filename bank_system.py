#!/usr/bin/env python
# -*- coding: utf8 -*-


import datetime
from time import strftime
from datetime import datetime
from tkinter import Label,Button

class datas:
    def __init__(self):
        self.activities = {"user_1": [0, []], "user_2": [ 0, []]}
        self.members = {"user_1": "1234", "user_2": "4321"}

    def request_data(self):
        return self.activities,self.members

    def user_data(self):
        self.user_names = []
        for i in self.activities:
            self.user_names.append(i)
        return self.user_names

    def add_activities(self, name, money, activities_name, transfer_name=None):
        if activities_name == "deposit":
            self.activities[name][0] = self.activities[name][0] + int(money)
            self.activities[name][1].append(
                "deposid " + str(money) + " " + datetime.today().strftime('%d-%m-%y  %H:%M:%S:%f'))
        elif activities_name == "withdraw":
            self.activities[name][0] = self.activities[name][0] - int(money)
            self.activities[name][1].append(
                "withdrawed " + str(money) + " " + datetime.today().strftime('%d-%m-%y  %H:%M:%S:%f'))
        elif activities_name == "transfer":
            self.activities[transfer_name][0] = self.activities[transfer_name][0] + int(money)
            self.activities[name][0] = self.activities[name][0] - int(money)
            self.activities[name][1].append("Transferred " + str(money) + " " + datetime.today().strftime('%d-%m-%y  %H:%M:%S:%f'))
            self.activities[transfer_name][1].append("Transferred to me from " +transfer_name + " " +str(money) + " " + datetime.today().strftime('%d-%m-%y  %H:%M:%S:%f'))

    def continuous_structures(self, choice):
        if choice == "one":
            print("|-----------------------------------|")
            print("     Basic Bank System v.01      ")
            print("|-----------------------------------|")
            print("   Mersin, Turkey " + datetime.today().strftime('%d-%m-%y  %H:%M:%S'))
            print("|-----------------------------------|")
            print("< Choose what do you want to do. >")
            print("< 1.Login > ")
            print("< 2.Exit > ")
        elif choice == "two":
            print("< ==================== Bank Services Avaible ==================== >")
            print("Choose Service")
            print("1. Withdraw Money")
            print("2. Deposit Money")
            print("3. Transfer Money")
            print("4. My Account Information")
            print("5. Logout")
            print("< =============================================================== >")

    def user_verification(self, user_name, user_passwd):
        if user_name in self.members:
            if self.members[username] == user_passwd:
                return True
            else:
                return False
        else:
            return False
class deposit_and_withdraw:
    def __init__(self, data):
        self.datas = data


class transfer_details:
    def __init__(self, data):
        self.datas = data
    def deposit(self, name):
        money = input("How much do you wish to deposite ? ")
        while int(money) < 1:
            print("Try Again...")
            money = input("How much do you wish to deposite ? ")
        self.datas.add_activities(name, money, "deposit")
        print("You have deposit " + money)

    def withdraw(self, name):
        activities,users = self.datas.request_data()
        money = input("How much do you wish to withdraw ? ")
        while int(money) > activities[name][0]:
            print("Try Again...")
            money = input("How much do you wish to withdraw ? ")
        self.datas.add_activities(name, money, "withdraw")
        print(money + " TL Has been withdrawed from your account")
    def transfer(self, name):
        activities,users = self.datas.request_data()
        user_names = []
        for i in users:
            user_names.append(i)
        transferName = input("For who do you wish to transfer to ?")
        if name in user_names and name != transferName:
            transferMoney = input("How much would like to transfer ? ")
            if int(transferMoney) < activities[name][0]:
                self.datas.add_activities(name, transferMoney, "transfer", transferName)
                print("Transferring " + transferMoney + "TL to " + transferName + "Succeeded.")
            else:
                print("Try Again...")
        else:
            print("Try Again...")

    def details(self, name, passwd):
        activities,users = self.datas.request_data()
        print("| __________________________ User Data __________________________ |")
        print("Date: " + datetime.today().strftime('%d-%m-%y'))
        print("Time: " + datetime.today().strftime('%H:%M:%S'))
        print("Your: " + name)
        print("Password: " + users[name])
        print("Balance : " + str(activities[name][0]))
        print("| _________________________ Transactions _________________________ |")
        for i in activities[name][1]:
            print(i)


if __name__ == "__main__":
    data = datas()
    operation = transfer_details(data)
    program_end = False
    while not (program_end):
        data.continuous_structures("one")
        operation = input(">>>")
        while operation != "1" and operation != "2":
            print("Try again...")
            operation = input(">>>")
        if operation == "1":
            keep_going_1 = True
            username = input("Enter your username: ")
            passwd = input("Enter your password:")
            while keep_going_1:
                if data.user_verification(username, passwd):
                    print("Login Success!")
                    print("Transferring...")
                    print("Hello " + username)
                    keep_going_2 = True
                    while keep_going_2:
                        data.continuous_structures("two")
                        choose = input(">>>")
                        while choose != "1" and choose != "2" and choose != "3" and choose != "4" and choose != "5":
                            print("Try again...")
                            choose = input(">>>")
                        if choose == "1":
                            operation.withdraw(username)
                        elif choose == "2":
                            operation.deposit(username)
                        elif choose == "3":
                            operation.transfer(username)
                        elif choose == "4":
                            operation.details(username, passwd)
                        else:
                            keep_going_1 = False
                            keep_going_2 = False
                else:
                    print("Try Again...")
                    username = input("Enter your username: ")
                    passwd = input("Enter your password:")


        else:
            program_end = True
