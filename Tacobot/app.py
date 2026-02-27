import tkinter as tk
import chat
# Create the main window
root = tk.Tk()
root.title("Hello World")

y=chat.xprint(chat.tet)
# Create a label widget to display the text
label = tk.Label(root, text=y)
label.pack()

# Start the main event loop
root.mainloop()