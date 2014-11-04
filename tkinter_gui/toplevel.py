#!/usr/bin/python

import Tkinter as tk

class Example(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.do_grab = tk.BooleanVar()
        cb = tk.Checkbutton(self, text="New window grabs all events", 
                            variable=self.do_grab, onvalue=True, offvalue=False)
        cb.pack()
        new_button = tk.Button(self, text="New window", command=self.on_click)
        new_button.pack()

    def on_click(self):
        self.top = tk.Toplevel(self)
        button = tk.Button(self.top, text="dismiss", command=self.top.destroy)
        do_grab = self.do_grab.get()

        if do_grab:
            label = tk.Label(self.top, wraplength=200,
                             text="This window grabs all events")
        else:
            label = tk.Label(self.top, wraplength = 200, 
                             text="This window does NOT grab all events")
        label.pack(fill="x")
        button.pack()

        if do_grab:
            self.top.grab_set()

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

