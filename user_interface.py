from tkinter import Tk

class App(Tk):
    def __init__(self, title: str):
        super().__init__()
        self.title(title)
        self.config(padx=200, pady=140)

app = App("Morse Code Translator")

app.mainloop()