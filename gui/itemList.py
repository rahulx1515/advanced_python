import tkinter as tk
# from tkinter import messagebox, ttk

root = tk.Tk()

def addItem():
    if entry1.get() != '':
        listbox.insert(tk.END, entry1.get())
        entry1.delete(0, tk.END)
def removeItem():
    listbox.delete(tk.ANCHOR)

entry1 = tk.Entry(root)
entry1.pack()

tk.Button(root, text='Add', command=addItem).pack()
tk.Button(root, text='Remove', command=removeItem).pack()

listbox = tk.Listbox(root)
listbox.pack()

# __name__ ==  '__main__'  ## module variable
root.mainloop() # to make responsive