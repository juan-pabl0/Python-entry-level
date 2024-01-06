import os

global balance
balance = 2000

def menu():
        
        os.system('cls')
        print("Welcome to the online bank system")
        print("what do you like to do")
        print("1- Deposit")
        print("2- Withdraw")
        print("3- View")
        print("4- Transfer")
        print("5- exit")
        option = input()
        if option == "1":
                deposit()
        elif  option =="2":
                withdraw()
        elif option == "3":
                view()
        elif option =="4":
                transfer()
        elif option =="5":
                print("thanks for using the system")
                exit()

def deposit():
        global balance
        print("how much do you want to deposit?")
        var = input("your value: ")
        deposit = int(var) 
        balance = balance + deposit 
        print("you choose to deposit", deposit)
        print("And your balance is" , balance)
        
        print("1- Return to menu or 0 to exit the program")
        op = input("type your option: ")
        if op == "1":
                menu()
        elif op == "0":
                print("thanks for your time :) ")
                exit()

                
def withdraw():           #seria una extraccion de dinero
        global balance
        x = True
        while  x == True:
                print("how much do you want to withdraw")
                var = input("your value: ")
                withdraw = int(var)
                if withdraw > balance:
                        print("your current balance is", balance)
                        print("the amount to withdraw is more than the amount balance in your account")
                        break
                else:
                        balance = balance - withdraw
                        print("your new balance is", balance)
                        x = False
        print("1- Return to menu /n 0 to exit the program")
        op = input()
        if op == "1":
                menu()
        elif op == "0":
                print("thanks for your time :) ")
                exit()
     
def view():
        global balance
        print("your current balance is", balance)
        print("1- Return to menu or 0 to exit the program")
        op = input()
        if op == "1":
                menu()
        elif op == "0":
                print("thanks for your time :) ")
                exit()

def transfer():
        global balance
        x = True
        while  x == True:
                print("how much do you want to transfer")
                var = input()
                transfer = int(var)
                if transfer > balance:
                        print("your current balance is {balance}")
                        print("the amount to transfer is more than the amount balance in your account")
                        break
                else:
                        balance -= transfer
                        print("your new balance", balance)
                        x = False
        print("1- Return to menu or to exit the program")
        op = input()
        if op == "1":
                menu()
        elif op == "0":
                print("thanks for your time :) ")
                exit()
                
        

