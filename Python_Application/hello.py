import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.good_night_there = tk.Button(self)
        self.good_night_there["text"] = "Good night\n(click me)"
        self.good_night_there["command"] = self.say_good_night
        self.good_night_there.pack(side="top")
        

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def say_good_night(self):
        print("good night.")
        self.good_night_there["text"] = "OK"


def main():
    root = tk.Tk()
    root.title("Tkinter test")
    root.geometry("640x480")
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()