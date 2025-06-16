from tkinter import ttk
from tkinter import *

class Supername:
    def __init__(self) -> None:
        
        self.root = Tk()
        self.super_name = StringVar()
        Label(self.root,text="HERO NAME GENERATOR",bg="green").grid(row=0,column=0)
        self.root.resizable(0,0)
        self.adjective_list = [
            "Super",
            "Lantern",
            "Doctor",
            "Inspector"
        ]        
        self.colour_options = [
            "Yellow",
            "Blue",
            "Orange",
            "Green",
            "Magenta"
        ]
        self.animal_options = [
            "Cat",
            "Dog",
            "Lion",
            "Tiger",
            "Dolphin"
        ]
        self.adjective_frame = Frame(self.root)
        self.combo_frame = Frame(self.root)
        self.display_frame = Frame(self.root)

        self.adjective_frame.grid(row=1,column=0)
        self.combo_frame.grid(row=2,column=0)
        self.display_frame.grid(row=3,column=0)

        self.adjective = StringVar()
        for index, ad in enumerate(self.adjective_list,start=1):
            button = ttk.Radiobutton(self.adjective_frame,text=ad,value=ad,variable=self.adjective)
            button.grid(row=index,column=0)

        self.colour = StringVar()  
        self.colour.set("")      
        self.colour_combo = ttk.Combobox(self.combo_frame,textvariable=self.colour)
        self.colour_combo['values'] = self.colour_options
        self.colour_combo.grid(row=0,column=0)

        self.animal = StringVar()  
        self.animal.set("")      
        self.animal_combo = ttk.Combobox(self.combo_frame,textvariable=self.animal,state="readonly")
        self.animal_combo['values'] = self.animal_options
        self.animal_combo.grid(row=1,column=0)

        self.go_go_gadjet_name = Button(self.display_frame,text="Go Go Gadjet Get Name",command=self.get_name)
        self.go_go_gadjet_name.grid(row=0,column=0)
        self.display = Label(self.display_frame,textvariable=self.super_name)
        self.display.grid(row=1,column=0,sticky='news')
    def get_name(self):
        self.super_name.set(f"{self.adjective.get()} {self.colour.get()} {self.animal.get()}")
super = Supername()
super.root.mainloop()
