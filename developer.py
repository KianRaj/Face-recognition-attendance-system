from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")


        title_lbl = Label(self.root,text = "DEVELOPER",font = ("times new roman",30,"bold"),bg="white",fg="darkred")
        title_lbl.place(x=0,y=0,width=1300,height=45)

        img_top = Image.open(r"college_images\bg.JPG")
        img_top = img_top.resize((1366,600),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1366,height=600)
   
# Frame
        main_frame = Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=800,y=0,width=450,height=500)

        
        img_top1 = Image.open(r"college_images\develop.jpg")
        img_top1 = img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=250,y=0,width=195,height=200)

#Developer info
        dev_label = Label(main_frame,text="Developer team:-",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=0,y=5)
        
        dev_label = Label(main_frame,text="Deepak,Aanand,Aman",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=0,y=30)

# image
        img3 = Image.open(r"college_images\developerr.jpg")
        img3 = img3.resize((445,290),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(main_frame,image=self.photoimg3)
        f_lbl.place(x=0,y=205,width=445,height=290)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()