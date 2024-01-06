"""1. Create an online banking system with the following features:

* Users must be able to log in with a username and password.
* If the user enters the wrong credentials three times, the system must lock them out.
* The initial balance in the bank account is $2000.
* The system must allow users to deposit, withdraw, view, and transfer money.
* The system must display a menu for users to perform transactions."""
    

import functions as fc
import os

print("Welcome enter your keys")
auth = False
correct_username = "juan"
correct_password = "1234"
x = 3
while auth == False and x != 0:
        input_username = input(str("Username: "))
        input_password = input(str("Password: "))
        if input_username == correct_username and input_password == correct_password:
                print("successfully entered")
                auth = True
                break
        else:
                x = x - 1
                print("Invalid keys you have",x, " tries left please try again")         

if auth == True:
        fc.menu()
else:
        print("thanks for your time :) ")


