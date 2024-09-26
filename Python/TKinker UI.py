import tkinter as tk

def say_hello():
    print("Hello, world!")

# Create the main window
root = tk.Tk()
root.title("Simple GUI")

# Create a button widget
hello_button = tk.Button(root, text="Say Hello", command=say_hello)
hello_button.pack(pady=20)

# Start the main event loop
root.mainloop()
