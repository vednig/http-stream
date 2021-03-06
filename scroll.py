import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style()
style.theme_use('clam')

# list the options of the style
# (Argument should be an element of TScrollbar, eg. "thumb", "trough", ...)
print(style.element_options("Horizontal.TScrollbar.thumb"))

# configure the style
style.configure("Horizontal.TScrollbar", gripcount=10,
                background="black", darkcolor="gray", lightcolor="black",
                troughcolor="black", bordercolor="black", arrowcolor="white")

hs = ttk.Scrollbar(root, orient="horizontal")
hs.place(x=5, y=5, width=150)
hs.set(0.2,0.3)

root.mainloop()
