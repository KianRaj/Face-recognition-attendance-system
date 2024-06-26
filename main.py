from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import os
from datetime import datetime
from time import strftime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendence
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

# 1st image
        img1 = Image.open(r"college_images\facial_recognition1.png")
        img1 = img1.resize((430,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=430,height=130)

# second image
        img2 = Image.open(r"college_images\facial_recognition2.png")
        img2 = img2.resize((430,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=430,y=0,width=430,height=130)
        
# 3rd image
        img3 = Image.open(r"college_images\facial_recognition3.png")
        img3 = img3.resize((430,130),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root,image=self.photoimg3)
        f_lbl.place(x=860,y=0,width=430,height=130)


# bg image
        img4 = Image.open(r"college_images\bg.jpg")
        img4 = img4.resize((1366,550),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1366,height=550)

        title_lbl = Label(bg_img,text = "FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font = ("times new roman",30,"bold"),bg="white",fg="darkred")
        title_lbl.place(x=0,y=0,width=1300,height=45)

# Time
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
            
        lbl = Label(title_lbl,font = ("times new roman",10,"bold"),bg="white",fg="darkgreen")
        lbl.place(x=0,y=0,width=80,height=50)
        time()

# student button
        img5 = Image.open(r"college_images\student_details2.jpg")
        img5 = img5.resize((180,180),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image = self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=80,width=180,height=180)

        b1 = Button(bg_img,text="Students Details",command=self.student_details,cursor="hand2",font = ("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=100,y=250,width=180,height=40)

# detect face button
        img6 = Image.open(r"college_images\face_detector1.jpg")
        img6 = img6.resize((180,180),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b2 = Button(bg_img,image = self.photoimg6,cursor="hand2",command=self.face_data)
        b2.place(x=400,y=80,width=180,height=180)

        b2 = Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font = ("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=400,y=250,width=180,height=40)


# Attendence face button
        img7 = Image.open(r"college_images\attendence.jpg")
        img7 = img7.resize((180,180),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b2 = Button(bg_img,image = self.photoimg7,cursor="hand2",command=self.attendence_data)
        b2.place(x=700,y=80,width=180,height=180)

        b2 = Button(bg_img,text="Attendence",cursor="hand2",command=self.attendence_data,font = ("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=700,y=250,width=180,height=40)


# Help Desk button
        img8 = Image.open(r"college_images\help_desk.jpg")
        img8 = img8.resize((180,180),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b2 = Button(bg_img,image = self.photoimg8,cursor="hand2",command=self.help_data)
        b2.place(x=1000,y=80,width=180,height=180)

        b2 = Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font = ("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=1000,y=250,width=180,height=40)


# Train Data Button
        img9 = Image.open(r"college_images\Train.jpg")
        img9 = img9.resize((180,180),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b2 = Button(bg_img,image = self.photoimg9,cursor="hand2",command=self.train_data)
        b2.place(x=100,y=300,width=180,height=180)

        b2 = Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font = ("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=100,y=470,width=180,height=40)


# Photos Button
        img10 = Image.open(r"college_images\photos.jpg")
        img10 = img10.resize((180,180),Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b2 = Button(bg_img,image = self.photoimg10,cursor="hand2",command=self.open_img)
        b2.place(x=400,y=300,width=180,height=180)

        b2 = Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font = ("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=400,y=470,width=180,height=40)


# Developer Button
        img11 = Image.open(r"college_images\developer.jpg")
        img11 = img11.resize((180,180),Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b2 = Button(bg_img,image = self.photoimg11,cursor="hand2",command=self.developer_data)
        b2.place(x=700,y=300,width=180,height=180)

        b2 = Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font = ("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=700,y=470,width=180,height=40)


# Exit Button
        img12 = Image.open(r"college_images\exit.jpg")
        img12 = img12.resize((180,180),Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b2 = Button(bg_img,image = self.photoimg12,cursor="hand2",command=self.iExit)
        b2.place(x=1000,y=300,width=180,height=180)

        b2 = Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font = ("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=1000,y=470,width=180,height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return


#Function buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
   
    def attendence_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)
   
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
   
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()