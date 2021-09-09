#Netflix type system demo - FakeFlix
import csv
import sys
import os
from subprocess import call

def main():
   menu()

#def clear():
    # check and make call for specific operating system
 #   _ = call('clear' if os.name =='posix' else 'cls')

def menu():
    print("************Welcome to FakeFlix Demo**************")
    print()

    choice = input("""
                      A: Please Register
                      B: Login
                      Q: Logout

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        register()
    elif choice == "B" or choice =="b":
        login()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either A or B")
        print("Please try again")
        clear()
        menu()

def register():
   print('kontol')
    
def login():
   pass

def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name =='posix' else 'cls')
    
#the program is initiated, so to speak, here
main()

