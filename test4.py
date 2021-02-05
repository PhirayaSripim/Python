import os
choice = 0
filename = " "

def menu():
    global choice
    print("Menu\n 1.Open Notepad\n 2. Open Write\n 3.Exit")
    choice = input("Select Menu :")

def opennotepad():
    filename = "C:\Windows\\notepad.exe"
    print("Memorandum writing %s" &filename)
    os.system(filename)

def Openwrite():
    filename = "C:\Windows\\write.exe"
    print("Write %s" &filename )
    os.system(filename)

while True:
    menu()
    if choice == "1":
        opennotepad()
    elif choice =="2":
        openwrite
    else:
        break
    