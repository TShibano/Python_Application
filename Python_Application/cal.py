import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_button(buttun):
        num = int(button[-1])
        self.button["text"] = num
        self.button["command"] = self.button

    def create_widgets(self):
        

        self.button9 = tk.Button(self)
        self.button9["text"] = "9"
        self.button9.pack(side="right")

        self.button8 = tk.Button(self)
        self.button8["text"] = "8"
        self.button8.pack(side="top")



def main():
    root = tk.Tk()
    root.geometry("400x320")
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()