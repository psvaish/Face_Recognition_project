from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        # ====================variables================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_std_name=StringVar()
        #1st
        img=Image.open(r"C:\Users\Pranathi.Induri\OneDrive\Desktop\Face Recognition Files\College_Photos\Student1.jpeg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
       #2nd
        img1=Image.open(r"C:\Users\Pranathi.Induri\OneDrive\Desktop\Face Recognition Files\College_Photos\Student2.jpeg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        #3rd
        img2=Image.open(r"C:\Users\Pranathi.Induri\OneDrive\Desktop\Face Recognition Files\College_Photos\Student3.jpeg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)
        #background image
        img3=Image.open(r"C:\Users\Pranathi.Induri\OneDrive\Desktop\Face Recognition Files\College_Photos\bgimg.jpeg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="Student Management System",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame =Frame(bg_img,bd=2,bg='white')
        main_frame.place(x=10,y=55,width=1500,height=600)

        #leftlabelframe
        Left_frame = LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text='Student Details',font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"C:\Users\Pranathi.Induri\OneDrive\Desktop\Face Recognition Files\College_Photos\Leftframe.jpeg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #currentcourse
        currentcourse_frame = LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text='Current course Information',font=("times new roman",12,"bold"))
        currentcourse_frame.place(x=15,y=150,width=720,height=115)

        #department
        dep_label=Label(currentcourse_frame,text='Department',font=("times new roman",13,"bold"),bg='white')
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(currentcourse_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state='readonly',width=20)
        dep_combo['values']=('Select Department','Computer Science','Information Technology','Civil Engineering','Mechanical Engineering')
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #courseLabel
        course_label=Label(currentcourse_frame,text='Course',font=("times new roman",13,"bold"),bg='white')
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(currentcourse_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state='readonly',width=20)
        course_combo['values']=('Select course','FE','SE','TE','BE')
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #yearlabel
        year_label=Label(currentcourse_frame,text='Year',font=("times new roman",13,"bold"),bg='white')
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(currentcourse_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state='readonly',width=20)
        year_combo['values']=('Select year','2020-2021','2021-2022','2022-2023','2023-2024')
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #SemesterLabel
        semester_label=Label(currentcourse_frame,text='Semester',font=("times new roman",13,"bold"),bg='white')
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(currentcourse_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state='readonly',width=20)
        semester_combo['values']=('Select semester','semester-1','semester-2')
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #StudentInformation
        classstudent_frame = LabelFrame(Left_frame,bd=2,bg='white',relief=RIDGE,text='Class Student Information',font=("times new roman",13,"bold"))
        classstudent_frame.place(x=5,y=235,width=720,height=315)

        #StudentIDLabel
        studentid_label=Label(classstudent_frame,text='StudentID:',font=("times new roman",13,"bold"),bg='white')
        studentid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentid_entry=ttk.Entry(classstudent_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

         #StudentName
        studentname_label=Label(classstudent_frame,text='Student Name:',font=("times new roman",13,"bold"),bg='white')
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(classstudent_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

         #Class Divisom
        classdivison_label=Label(classstudent_frame,text='Class Divison:',font=("times new roman",13,"bold"),bg='white')
        classdivison_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(classstudent_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state='readonly',width=20)
        div_combo['values']=('A','B','C')
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)

         #Rollno
        rollno_label=Label(classstudent_frame,text='Rollno:',font=("times new roman",13,"bold"),bg='white')
        rollno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        rollno_entry=ttk.Entry(classstudent_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label=Label(classstudent_frame,text='Gender:',font=("times new roman",13,"bold"),bg='white')
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(classstudent_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state='readonly',width=20)
        gender_combo['values']=('Male','Female','Other')
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #DOB
        dob_label=Label(classstudent_frame,text='DOB:',font=("times new roman",13,"bold"),bg='white')
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(classstudent_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #email
        email_label=Label(classstudent_frame,text='Email:',font=("times new roman",13,"bold"),bg='white')
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(classstudent_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phoneno
        phoneno_label=Label(classstudent_frame,text='Phone no:',font=("times new roman",13,"bold"),bg='white')
        phoneno_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phoneno_entry=ttk.Entry(classstudent_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phoneno_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #address
        address_label=Label(classstudent_frame,text='Address:',font=("times new roman",13,"bold"),bg='white')
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(classstudent_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #teachername
        teachername_label=Label(classstudent_frame,text='Teacher Name:',font=("times new roman",13,"bold"),bg='white')
        teachername_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teachername_entry=ttk.Entry(classstudent_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teachername_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(classstudent_frame,variable=self.var_radio1,text = "Take Photo Sample",value="Yes")
        radionbtn1.grid(row=6,column=0)

        radionbtn2=ttk.Radiobutton(classstudent_frame,variable=self.var_radio1,text = "No Photo Sample",value="No")
        radionbtn2.grid(row=6,column=1)

        #buttons frame
        btn_frame=Frame(classstudent_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=220,width=715,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=17,command=self.delete_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(classstudent_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=255,width=715,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)












       





        #rightlabelframe
        Right_frame = LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text='Student Details',font=("times new roman",13,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        img_right=Image.open(r"C:\Users\Pranathi.Induri\OneDrive\Desktop\Face Recognition Files\College_Photos\Rightframe.jpeg")
        img_right=img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #===searchsystem====
        Search_frame = LabelFrame(Right_frame,bd=2,bg='white',relief=RIDGE,text='Search System',font=("times new roman",13,"bold"))
        Search_frame.place(x=5,y=135,width=700,height=70)


        Search_label=Label(Search_frame,text='Search by:',font=("times new roman",15,"bold"),bg='red',fg='white')
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        Search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state='readonly',width=15)
        Search_combo['values']=('Select','Roll no','Phone no')
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3,padx=4)

        Showall_btn=Button(Search_frame,text="Showall",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Showall_btn.grid(row=0,column=4,padx=4)
        #====TableFrame=========
        Table_frame = Frame(Right_frame,bd=2,bg='white',relief=RIDGE)
        Table_frame.place(x=5,y=210,width=710,height=350)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(Table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Divison")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phoneno")
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
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

##########=========================function declaration==========================############################

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="test@123",database="face_recognizer") #change later
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
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
                messagebox.show("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)




    #=========================================fetch data===============================#
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="test@123",database="face_recognizer") #change later
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
        conn.commit()
        conn.close()

    #===========================================get cursor================================
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
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


    #==============update data =========================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="test@123",database="face_recognizer") #change later
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                    self.var_div.get(),
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
                    if not Update:
                        messagebox.showinfo("Update failed","Student details failed to update",parent=self.root)
                    messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



    ########delete #####################
    
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Details Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="test@123",database="face_recognizer") #change later
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
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
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    #####reset button####
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_dep.set("Select Department")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")



#================================= Generate dataset  or take photo sample ==================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="test@123",database="face_recognizer") #change later
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                    self.var_div.get(),
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

            #========================== Load predefined data on face frontals from opencv====================

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor =1.3
                    #minimum neighbor = 5

                    for(x,y,w,h) in faces:
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
                messagebox.showinfo("Result","Generating data set completed !")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)







if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()