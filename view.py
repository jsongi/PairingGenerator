import tkinter as tk
from tkinter import font

#Initialize main window
root = tk.Tk()
root.title("Pairing Generator")
root.geometry("1280x720")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

def newWindow(root, choice):
    #hide the main window
    root.withdraw()

    if choice != "Generate Groups":
        addRemoveWindow(choice)
    else:
        generateGroupsWindow(choice)

def addRemoveWindow(choice):
    #Certain buttons remain constant, but their functions change, and output will differ
    return #placeholder

def generateGroupsWindow(choice):
    return #placeholder

def handleSelection(choice):
    match choice:
        case "Add Person":
            newWindow(choice)
        case "Remove Person":
            newWindow(choice)
        case "Add As Organizer":
            newWindow(choice)
        case "Remove As Organizer":
            newWindow(choice)
        case "Generate Groups":
            newWindow(choice)
        case _:
            print("ERROR")    

def initializeView():
    selected_option = tk.StringVar()
    selected_option.set("Select Option") 

    options = ["Add Person", "Remove Person", "Add As Organizer", "Remove As Organizer", "Generate Groups"]
    dropdown = tk.OptionMenu(root, selected_option, *options, command=handleSelection)
    dropdown.pack(pady=40)
    
    #Configuring dropdown size
    dropdown.grid(row=0,column=0, padx=60, pady=60, sticky="w")
    dropdown.config(font=font.Font(size=20))
    menu = dropdown["menu"]
    menu.config(font=font.Font(size=15))

    root.mainloop()