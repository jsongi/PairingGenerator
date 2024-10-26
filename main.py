import tkinter as tk

def newWindow():
    #hide the main window
    root.withdraw()

    newWindow = tk.Toplevel(root)
    newWindow.title("New Window")
    newWindow.geometry("300x200")

    label = tk.Label(newWindow, text="This is a new window!")
    label.pack(pady=20)

    back_button = tk.Button(newWindow, text="Go Back", command=lambda: exitWindow(new_window))
    back_button.pack()

def exitWindow(window):
    window.destroy()
    #show the main window again
    root.deiconify()

root = tk.Tk()
root.title("Pairing Generator")
root.geometry("1280x780")

button = tk.Button(root, text="Open New Window", command=newWindow)
button.pack(pady=20)

root.mainloop()
    