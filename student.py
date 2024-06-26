from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

# variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_reg_no=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

# 1st image
        img1 = Image.open(r"college_images\student1.png")
        img1 = img1.resize((430,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=430,height=130)
# second image
        img2 = Image.open(r"college_images\student2.jpg")
        img2 = img2.resize((430,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=430,y=0,width=430,height=130)
# 3rd image
        img3 = Image.open(r"college_images\student3.jpg")
        img3 = img3.resize((430,130),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root,image=self.photoimg3)
        f_lbl.place(x=860,y=0,width=430,height=130)


# bg image
        img4 = Image.open(r"college_images\bg.jpg")
        img4 = img4.resize((1366,638),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1366,height=638)

        title_lbl = Label(bg_img,text = "STUDENT MANAGEMENT SYSTEM",font = ("times new roman",30,"bold"),bg="white",fg="darkred")
        title_lbl.place(x=0,y=0,width=1300,height=45)

# Frame
        main_frame = Frame(bg_img,bd=2)
        main_frame.place(x=5,y=50,width=1260,height=463)

# left label frame
        Left_frame = LabelFrame(main_frame,bd = 2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=5,width=610,height=450)

        img_left = Image.open(r"college_images\student_details1.jpg")
        img_left = img_left.resize((610,100),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=600,height=100)

# current course information
        current_course_frame = LabelFrame(Left_frame,bd = 2,bg="white",relief=RIDGE,text="current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=102,width=600,height=70)

        #Department
        dep_label = Label(current_course_frame,text="Department",font=("times new roman",10,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),width=20,state="readonly")
        dep_combo["values"]=("Select Department","CSE","MECH","CIVIL","EEE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=1,sticky=W)
       
        #Course
        course_label = Label(current_course_frame,text="Course",font=("times new roman",10,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",10,"bold"),width=20,state="readonly")
        course_combo["values"]=("Select Course","BE","B.TECH")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=1,sticky=W)
       
       
        #Year
        year_label = Label(current_course_frame,text="Year",font=("times new roman",10,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",10,"bold"),width=20,state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=1,sticky=W)
      
      
        #Semester
        semester_label = Label(current_course_frame,text="Semester",font=("times new roman",10,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",10,"bold"),width=20,state="readonly")
        semester_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=1,sticky=W)


# Class student information
        class_student_frame = LabelFrame(Left_frame,bd = 2,bg="white",relief=RIDGE,text="Class student information",font=("times new roman",10,"bold"))
        class_student_frame.place(x=5,y=172,width=600,height=254)

        #Student Id
        studentId_label = Label(class_student_frame,text="StudentID",font=("times new roman",10,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=2,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=19,font=("times new roman",10,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=2,sticky=W)
       
       
        #Student Name
        studentName_label = Label(class_student_frame,text="Student Name",font=("times new roman",10,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=2,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=19,font=("times new roman",10,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=2,sticky=W)
      
      
        #Registration no
        reg_no_label = Label(class_student_frame,text="Reg no",font=("times new roman",10,"bold"),bg="white")
        reg_no_label.grid(row=1,column=0,padx=10,pady=2,sticky=W)

        reg_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_reg_no,width=19,font=("times new roman",10,"bold"))
        reg_no_entry.grid(row=1,column=1,padx=10,pady=2,sticky=W)     
       
        #Roll No
        roll_no_label = Label(class_student_frame,text="Roll No",font=("times new roman",10,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=2,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=19,font=("times new roman",10,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=2,sticky=W)
     
     
        #Gender
        gender_label = Label(class_student_frame,text="Gender",font=("times new roman",10,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=2,sticky=W)

        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",10,"bold"),width=17,state="readonly")
        gender_combo["values"]=("male","female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=2,sticky=W)
     
        #DOB
        dob_label = Label(class_student_frame,text="DOB",font=("times new roman",10,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=2,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=19,font=("times new roman",10,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=2,sticky=W)
      
      
        #Email
        email_label = Label(class_student_frame,text="Email",font=("times new roman",10,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=2,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=19,font=("times new roman",10,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=2,sticky=W)
     
     
        #Phone no
        phone_label = Label(class_student_frame,text="Phone no",font=("times new roman",10,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=2,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=19,font=("times new roman",10,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=2,sticky=W)
       
       
        #Address
        address_label = Label(class_student_frame,text="Address",font=("times new roman",10,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=2,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=19,font=("times new roman",10,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=2,sticky=W)
        
        
        #Teacher name
        teacher_label = Label(class_student_frame,text="Teacher name",font=("times new roman",10,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=2,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=19,font=("times new roman",10,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=2,sticky=W)
       
#radio Buttons
        self.var_radio1=StringVar()
        Radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take photo sample",value="yes")
        Radiobtn1.grid(row=5,column=0)
      
        self.var_radio2=StringVar()
        Radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample",value="no")
        Radiobtn2.grid(row=5,column=1)


# button frame
        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg= "white")
        btn_frame.place(x=0,y=166,width=595,height=35)

        # Save button
        save_btn= Button(btn_frame,text="Save",width=16,command=self.add_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        # Update button
        update_btn= Button(btn_frame,text="Update",width=16,command=self.update_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
       
        # delete button
        delete_btn= Button(btn_frame,text="Delete",width=16,command=self.delete_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
       
        # reset button
        reset_btn= Button(btn_frame,text="Reset",width=16,command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
       
# button frame
        btn_frame1 = Frame(class_student_frame,bd=2,relief=RIDGE,bg= "white")
        btn_frame1.place(x=0,y=200,width=595,height=35)

        # take_photo button
        take_photo_btn= Button(btn_frame1,command=self.generate_dataset,text="Take photo",width=33,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)
        
        # update_photo button
        update_photo_btn= Button(btn_frame1,text="Update photo",width=33,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)


# right label frame
        Right_frame = LabelFrame(main_frame,bd = 2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=640,y=5,width=600,height=450)

        img_right = Image.open(r"college_images\student_details3.jpg")
        img_right = img_right.resize((610,100),Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=600,height=100)


#-----*****Search system*****-----
        search_frame = LabelFrame(Right_frame,bd = 2,bg="white",relief=RIDGE,text="Search system",font=("times new roman",10,"bold"))
        search_frame.place(x=5,y=100,width=590,height=80)

        #search
        search_label = Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),fg="white",bg="red")
        search_label.grid(row=0,column=0,padx=10,pady=2,sticky=W)

        search_combo = ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=12,state="readonly")
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        phone_entry=ttk.Entry(search_frame,width=12,font=("times new roman",12,"bold"))
        phone_entry.grid(row=0,column=2,padx=10,pady=2,sticky=W)

        # search button
        search_btn= Button(search_frame,text="Delete",width=12,font=("times new roman",11,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=2)
       
        # show all button
        showAll_btn= Button(search_frame,text="Reset",width=12,font=("times new roman",11,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=2)


#-----*****Table frame*****-----
        table_frame = LabelFrame(Right_frame,bd = 2,bg="white",relief=RIDGE,font=("times new roman",10,"bold"))
        table_frame.place(x=5,y=180,width=590,height=245)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","reg_no","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("reg_no",text="Registration No")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("reg_no",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    

# function declaration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Pk843435@123",database="face_recognition_db")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_reg_no.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)



#*************Fetch data***********

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Pk843435@123",database="face_recognition_db")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data= my_cursor.fetchall()
        
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

#********Get corsor******
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_reg_no.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

 
 #*******update function*******
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                update= messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Pk843435@123",database="face_recognition_db")
                    my_cursor=conn.cursor()
                    my_cursor.execute("UPDATE student SET dep=%s,course=%s,year=%s,semester=%s,student_name=%s,reg_no=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photo=%s WHERE student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_reg_no.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                        
                        ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("error",f"Due to:{str(es)}",parent=self.root)


#*******Delete Function******
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student data?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Pk843435@123",database="face_recognition_db")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("error",f"Due to:{str(es)}",parent=self.root)

                
#*******Reset Function******
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_reg_no.set(""),
        self.var_roll.set(""),
        self.var_gender.set("male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")
        
#*****Generate data set or Take photo samples*******
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Pk843435@123",database="face_recognition_db")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("UPDATE student SET dep=%s,course=%s,year=%s,semester=%s,student_name=%s,reg_no=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photo=%s WHERE student_id=%s",(
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_reg_no.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()==id+1
                        ))
                conn.commit()       
                self.fetch_data()
                self.reset_data()
                conn.close()

#**************Load predefined data on face frontals from opencv***********
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor= 1.3
                    #minimum neighbour= 5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed ! ! !")
            except Exception as es:
                messagebox.showerror("error",f"Due to:{str(es)}",parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()