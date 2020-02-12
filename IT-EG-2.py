from tkinter import*
import datetime

def main():
    root=Tk()
    app = Windows1(root)

class Windows1:
    def __init__(self,root):
        self.root =root
        self.root.title("RALIWAY BOOKING")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg ="blue")
        self.root.pack()


root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label='BOOK TICKET',menu=filemenu)
menu.add_cascade(label='REGISTER',menu=filemenu)
menu.add_cascade(label='LOGIN',menu=filemenu)



L=Label(root, text="Enter  first name:").grid(row=0)
L=Label(root, text="Enter last name:").grid(row=1)
L=Label(root, text="Enter email id:").grid(row=2)
L=Label(root, text="Enter contact no:").grid(row=3)

e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
e4=Entry(root)



e1.grid(row=0,column=0)
e2.grid(row=0,column=1)
e3.grid(row=0,column=2)
e4.grid(row=0,column=3)

mainloop()
