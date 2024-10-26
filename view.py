import tkinter as tk

def newWindow(root):
    #hide the main window
    root.withdraw()

    newWindow = tk.Toplevel(root)
    newWindow.title("New Window")
    newWindow.geometry("1280x720")

    label = tk.Label(newWindow, text="This is a new window!")
    label.pack(pady=20)

    back_button = tk.Button(newWindow, text="Go Back", command=lambda: exitWindow(root, newWindow))
    back_button.pack()

def exitWindow(root, window):
    window.destroy()
    #show the main window again
    root.deiconify()

def initializeView():
    root = tk.Tk()
    root.title("Pairing Generator")
    root.geometry("1280x720")

    selected_option = tk.StringVar()
    selected_option.set("Select an option") 

    options = ["Add Person", "Remove Person", "Add As Organizer", "Remove As Organizer", "Generate Groups"]
    dropdown = tk.OptionMenu(root, selected_option, *options, command=newWindow)
    dropdown.pack(pady=20)

    root.mainloop()