from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text = "HELP DESK",font = ("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1300,height=45)

        img_top = Image.open(r"college_images\help.jpeg")
        img_top = img_top.resize((1366,580),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1366,height=580)

#Developer info
        dev_label = Label(f_lbl,text="Email:dks843435@gmail.com",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=500,y=130)
        dev_label = Label(f_lbl,text="Phone:9128729421",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=560,y=170)
        

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()