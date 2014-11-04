import Tkinter as tk
import ttk

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.size=5
        self.vars = {}
        for i in range(self.size):
            self.vars[i] = tk.StringVar()
            entry = ttk.Entry(self, textvariable=self.vars[i])
            entry.pack(side="top", fill="x")
            self.vars[i].trace("w", self.callback)

        # this entry will show the other values as a list
        self.e0Var = tk.StringVar()
        self.e0 = ttk.Entry(self, textvariable=self.e0Var)
        self.e0.pack(side="top", fill="x", pady=(4,0))

        # call the callback once to establish the initial value
        self.callback()

    def callback(self, *args):
        values = []
        for i in range(self.size):
            values.append(self.vars[i].get())
        # make a comma separated list and store in e0Var
        self.e0Var.set(str(values))

app = App()
app.mainloop()
