#!/usr/bin/python
from Tkinter import *

def size_for_alternatives(parent, kids):
    w = max([k.winfo_reqwidth() for k in kids])
    h = max([k.winfo_reqheight() for k in kids])
    print ([k.winfo_reqwidth() for k in kids]), w
    print ([k.winfo_reqheight() for k in kids]), h
    parent.pack_propagate(0)
    parent.grid_propagate(0)
    parent.configure(width=w, height=h)

def swap():
    if v.get():
        e.pack_forget()
        mb.pack(anchor="w", side="left")

    else:
        mb.pack_forget()
        e.pack(anchor="w", side="left")
        e.focus()
t = Tk()
v = IntVar(t)
c = Checkbutton(t, command=swap, text="Order from menu?", variable=v)
c.pack(anchor="w")

f1 = Frame(t)
l = Label(f1, text="Your order:")
l.pack(side="left")
f = Frame(f1)
f.pack(side="left")
e = Entry(f, width=18)
mb = Menubutton(f, width=8, text="eggs", indicatoron=1, relief="sunken", anchor="w")
m = Menu(mb, tearoff=0); mb.configure(menu=m)
for s in "eggs bacon sausage spam".split():
    m.add_command(label=s, command=lambda s=s: mb.configure(text=s))
f.after_idle(lambda: size_for_alternatives(f, (e, mb)))

f.pack()
f1.pack()
swap()

b = Button(t, text="Place order", command=t.destroy); b.pack(side="top")

f.mainloop()
