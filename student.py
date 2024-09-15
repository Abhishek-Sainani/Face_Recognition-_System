from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # First image
        img = Image.open(r"C:\Users\Abhishek Sainani\Desktop\images of project\photo.jpg")
        img = img.resize((533, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=533, height=130)

        # Second image
        img1 = Image.open(r"C:\Users\Abhishek Sainani\Desktop\images of project\photo.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=533, y=0, width=500, height=130)

        # Third image
        img2 = Image.open(r"C:\Users\Abhishek Sainani\Desktop\images of project\photo.jpg")
        img2 = img2.resize((533, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1033, y=0, width=533, height=130)

        # Background image
        img3 = Image.open("background.jpg")
        img3 = img3.resize((1600, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1600, height=710)

        # Title
        title_lbl = Label(bg_img, text="STUDENT DETAILS", font=("Times New Roman", 35, "bold"), bg="yellow", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=35)

        # Main frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=40, width=1610, height=690)

        # Left label frame
        LEFT_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("Times New Roman", 12, "bold"))
        LEFT_frame.place(x=10, y=5, width=750, height=605)

        img_left = Image.open(r"C:\Users\Abhishek Sainani\Desktop\images of project\photo.jpg")
        img_left = img_left.resize((550, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(LEFT_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=740, height=130)

        # Current course
        current_course_frame = LabelFrame(LEFT_frame, bd=2, bg="white", relief=RIDGE, text="Course Information", font=("Times New Roman", 12, "bold"))
        current_course_frame.place(x=5, y=130, width=720, height=110)

        # Department
        dep_label = Label(current_course_frame, text="Department", font=("Times New Roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, font=("Times New Roman", 12, "bold"), width=17)
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course", font=("Times New Roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, font=("Times New Roman", 12, "bold"), width=17)
        course_combo["values"] = ("Select Course", "Computer", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=("Times New Roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, font=("Times New Roman", 12, "bold"), width=17)
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=("Times New Roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, font=("Times New Roman", 12, "bold"), width=17)
        semester_combo["values"] = ("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)
         # student information
        class_Student_frame = LabelFrame(LEFT_frame, bd=2, bg="white", relief=RIDGE, text="Class Student  Information", font=("Times New Roman", 12, "bold"))
        class_Student_frame.place(x=5, y=240, width=720, height=680)
        #student id

        studentId = Label(class_Student_frame, text="StudentID:", font=("Times New Roman", 12, "bold"), bg="white")
        studentId.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,width=20,font=("Times New Roman", 12, "bold"))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)
        #student name
        StudentName_label = Label(class_Student_frame, text="Student Name:", font=("Times New Roman", 12, "bold"), bg="white")
        StudentName_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        StudentName_entry_entry=ttk.Entry(class_Student_frame,width=20,font=("Times New Roman", 12, "bold"))
        StudentName_entry_entry.grid(row=0,column=3,padx=10,sticky=W)

        #class division
        class_div_label = Label(class_Student_frame, text="Class_division:", font=("Times New Roman", 12, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        class_div_entry_entry=ttk.Entry(class_Student_frame,width=20,font=("Times New Roman", 12, "bold"))
        class_div_entry_entry.grid(row=1,column=1,padx=10,sticky=W)

        #Roll No
        Roll_no_label = Label(class_Student_frame, text="Roll_No:", font=("Times New Roman", 12, "bold"), bg="white")
        Roll_no_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        Roll_no_entry_entry=ttk.Entry(class_Student_frame,width=20,font=("Times New Roman", 12, "bold"))
        Roll_no_entry_entry.grid(row=1,column=3,padx=10,sticky=W)
        # Gender
        Gender_label = Label(class_Student_frame, text="Gender:", font=("Times New Roman", 12, "bold"), bg="white")
        Gender_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        Gender_entry_entry=ttk.Entry(class_Student_frame,width=20,font=("Times New Roman", 12, "bold"))
        Gender_entry_entry.grid(row=2,column=1,padx=10,sticky=W)
        #DOB:
        DOB_label = Label(class_Student_frame, text="DOB:", font=("Times New Roman", 12, "bold"), bg="white")
        DOB_label.grid(row=2, column=2, padx=10, pady=10, sticky=W)

        DOB_entry_entry=ttk.Entry(class_Student_frame,width=20,font=("Times New Roman", 12, "bold"))
        DOB_entry_entry.grid(row=2,column=3,padx=10,sticky=W)


        #Email
        Email_label = Label(class_Student_frame, text="Email:", font=("Times New Roman", 12, "bold"), bg="white")
        Email_label.grid(row=3, column=2, padx=10, pady=10, sticky=W)

        Email_entry_entry=ttk.Entry(class_Student_frame,width=20,font=("Times New Roman", 12, "bold"))
        Email_entry_entry.grid(row=3,column=3,padx=10,sticky=W)
        # phone no
        Phone_No_label = Label(class_Student_frame, text="Phone_No:", font=("Times New Roman", 12, "bold"), bg="white")
        Phone_No_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        Phone_No_entry_entry=ttk.Entry(class_Student_frame,width=20,font=("Times New Roman", 12, "bold"))
        Phone_No_entry_entry.grid(row=3,column=1,padx=10,sticky=W)

        # Address
        Address_label = Label(class_Student_frame, text="Address:", font=("Times New Roman", 12, "bold"), bg="white")
        Address_label.grid(row=4, column=2, padx=10, pady=10, sticky=W)

        Address_entry_entry=ttk.Entry(class_Student_frame,width=20,font=("Times New Roman", 12, "bold"))
        Address_entry_entry.grid(row=4,column=3,padx=10,sticky=W)
        #Teacher name
        Teacher_Name_label = Label(class_Student_frame, text="Teacher_Name", font=("Times New Roman", 12, "bold"), bg="white")
        Teacher_Name_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)

        Teacher_Name_entry_entry=ttk.Entry(class_Student_frame,width=20,font=("Times New Roman", 12, "bold"))
        Teacher_Name_entry_entry.grid(row=4,column=1,padx=10,sticky=W)

        #radio buttons
        Radiobtn1=ttk.Radiobutton(class_Student_frame,text="take Phot Sample",value="Yes")
        Radiobtn1.grid(row=5,column=0)
        Radiobtn2=ttk.Radiobutton(class_Student_frame,text="No photo sample",value="Yes")
        Radiobtn2.grid(row=5,column=1)
        

        #buttones Frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=250,width=720,height=40)
#save button 
        save_btn=Button(btn_frame,width=17,text="Save",font=("Times New Roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,)
#update button
        update=Button(btn_frame,width=17,text="Update",font=("Times New Roman",13,"bold"),bg="blue",fg="white")
        update.grid(row=0,column=1,)
#delete button
        delete=Button(btn_frame,width=17,text="Delete",font=("Times New Roman",13,"bold"),bg="blue",fg="white")
        delete.grid(row=0,column=2,)
#reset button  
        reset=Button(btn_frame,width=17,text="reset",font=("Times New Roman",13,"bold"),bg="blue",fg="white")
        reset.grid(row=0,column=3,)

        
#buttones Frame
        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=290,width=720,height=40)


        
        Take_photo_btn=Button(btn_frame1,width=34,text="Take photo Sample",font=("Times New Roman",13,"bold"),bg="blue",fg="white")
        Take_photo_btn.grid(row=0,column=0,)

        update_photo_btn=Button(btn_frame1,width=34,text="Update photo Sample",font=("Times New Roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1,)







        # Right label frame
        RIGHT_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("Times New Roman", 12, "bold"))
        RIGHT_frame.place(x=770, y=10, width=740, height=580)

        img_right = Image.open(r"C:\Users\Abhishek Sainani\Desktop\images of project\photo.jpg")
        img_right = img_right.resize((550, 130), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(RIGHT_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=740, height=130)

        #============search system ========
        Search_frame = LabelFrame(RIGHT_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("Times New Roman", 12, "bold"))
        Search_frame.place(x=5, y=135, width=740, height=70)

        #label of search
        search_label = Label(Search_frame, text="Search by", font=("Times New Roman", 15, "bold"), bg="red",fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        search_combo = ttk.Combobox(Search_frame, font=("Times New Roman", 12, "bold"), width=17)
        search_combo["values"] = ("Select ","Roll_NO", "Phone_no",)
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        Search_entry=ttk.Entry(Search_frame,width=20,font=("Times New Roman", 12, "bold"))
        Search_entry.grid(row=0,column=2,padx=10,sticky=W)

        search=Button(Search_frame,width=13,text="Search",font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        search.grid(row=0,column=3,padx=4)
        showAll=Button(Search_frame,width=13,text="Show All",font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        showAll.grid(row=0,column=4,padx=4)
#==========table frame
        table_frame = LabelFrame(RIGHT_frame, bd=2, bg="white")
        table_frame.place(x=5, y=210, width=740, height=350)
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,
    columns=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"),
    xscrollcommand=scroll_x.set,
    yscrollcommand=scroll_y.set
)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Year")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Divison")
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
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)


        self.student_table.pack(fill=BOTH,expand=1)
        
        
        


       


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
