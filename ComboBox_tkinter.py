import tkinter
from tkinter import ttk

form =tkinter.Tk()
form.geometry("700x500")

cbx1 = ttk.Combobox(form ,values = ("algiers", "annaba","oran"))
cbx1.pack()
cbx2 = ttk.Combobox(form, value =("london","leeds","birmingham"),state ="readonly")
cbx2.pack()
def f():
    print(cbx1.get())

ttk.Button(form,text = "ok" ,command = f).pack()

form.mainloop()
