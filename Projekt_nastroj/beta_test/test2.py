import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self):
        list=["a","b","c"]
        tk.Tk.__init__(self)
        for i in list:
            text=i+"get"
            self.entry = tk.Entry(self)
            self.entry.pack()
        self.button = tk.Button(self, text=text, command=self.on_button(list))
        self.button.pack()

    def on_button(self,list):
        for i in list:
            print(self.entry.get())

app = SampleApp()
app.mainloop()