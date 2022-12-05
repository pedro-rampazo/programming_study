from tkinter import *
from tkinter import ttk

def sum_calculator(*args):
    try:
        val1 = value1.get()
        val2 = value2.get()
        sum_value.set(val1 + val2)
    except ValueError:
        pass

root = Tk()
root.title("Sum Calculator")

mainframe = ttk.Frame(root, padding="5 5 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Value1:").grid(column=1, row=1)
ttk.Label(mainframe, text="Value2:").grid(column=1, row=2)
ttk.Label(mainframe, text="RESULT:").grid(column=1, row=3)

sum_value = IntVar()
ttk.Label(mainframe, textvariable=sum_value).grid(column=2, row=3)

value1 = IntVar()
value1_entry = ttk.Entry(mainframe, width=7, textvariable=value1)
value1_entry.grid(column=2, row=1)

value2 = IntVar()
value2_entry = ttk.Entry(mainframe, width=7 ,textvariable=value2)
value2_entry.grid(column=2, row=2)

ttk.Button(mainframe, text="Sum", command=sum_calculator).grid(column=3, row=3)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

value1_entry.focus()
root.bind("<Return>", sum_calculator)

root.mainloop()