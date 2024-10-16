from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_name = StringVar()
        self.var_std_id = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_radio = StringVar()

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

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("Times New Roman", 12, "bold"), width=17)
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row= 0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course", font=("Times New Roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("Times New Roman", 12, "bold"), width=17)
        course_combo["values"] = ("Select Course", "Computer", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=("Times New Roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("Times New Roman", 12, "bold"), width=17)
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=("Times New Roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("Times New Roman", 12, "bold"), width=17)
        semester_combo["values"] = ("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Student information
        class_Student_frame = LabelFrame(LEFT_frame, bd=2, bg="white", relief=RIDGE, text="Class Student  Information", font=("Times New Roman", 12, "bold"))
        class_Student_frame.place(x=5, y=240, width=720, height=680)

        # Student ID
        studentId_label = Label(class_Student_frame, text="Student ID:", font=("Times New Roman", 12, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        studentID_entry = ttk.Entry(class_Student_frame, textvariable=self.var_std_id, width=20, font=("Times New Roman", 12, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, sticky=W)

        # Student Name
        StudentName_label = Label(class_Student_frame, text="Student Name:", font=("Times New Roman", 12, "bold"), bg="white")
        StudentName_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        StudentName_entry = ttk.Entry(class_Student_frame, textvariable=self.var_std_name, width=20, font=("Times New Roman", 12, "bold"))
        StudentName_entry.grid(row=0, column=3, padx=10, sticky=W)

        # Class Division
        class_div_label = Label(class_Student_frame, text="Class Division:", font=("Times New Roman", 12, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        class_div_entry = ttk.Entry(class_Student_frame, textvariable=self.var_div, width=20, font=("Times New Roman", 12, "bold"))
        class_div_entry.grid(row=1, column=1, padx=10, sticky=W)

        # Roll No
        Roll_no_label = Label(class_Student_frame, text="Roll No:", font=("Times New Roman", 12, "bold"), bg="white")
        Roll_no_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        Roll_no_entry = ttk.Entry(class_Student_frame, textvariable=self.var_roll, width=20, font=("Times New Roman", 12, "bold"))
        Roll_no_entry.grid(row=1, column=3, padx=10, sticky=W)

        # Gender
        Gender_label = Label(class_Student_frame, text="Gender :", font=("Times New Roman", 12, "bold"), bg="white")
        Gender_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        Gender_entry = ttk.Entry(class_Student_frame, textvariable=self.var_gender, width=20, font=("Times New Roman", 12, "bold"))
        Gender_entry.grid(row=2, column=1, padx=10, sticky=W)

        # DOB
        DOB_label = Label(class_Student_frame, text="DOB:", font=("Times New Roman", 12, "bold"), bg="white")
        DOB_label.grid(row=2, column=2, padx=10, pady=10, sticky=W)

        DOB_entry = ttk.Entry(class_Student_frame, textvariable=self.var_dob, width=20, font=("Times New Roman", 12, "bold"))
        DOB_entry.grid(row=2, column=3, padx=10, sticky=W)

        # Email
        Email_label = Label(class_Student_frame, text="Email:", font=("Times New Roman", 12, "bold"), bg="white")
        Email_label.grid(row=3, column=2, padx=10, pady=10, sticky=W)

        Email_entry = ttk.Entry(class_Student_frame, textvariable=self.var_email, width=20, font=("Times New Roman", 12, "bold"))
        Email_entry.grid(row=3, column=3, padx=10, sticky=W)

        # Phone No
        Phone_No_label = Label(class_Student_frame, text="Phone No:", font=("Times New Roman", 12, "bold"), bg="white")
        Phone_No_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        Phone_No_entry = ttk.Entry(class_Student_frame, textvariable=self.var_phone, width=20, font=("Times New Roman", 12, "bold"))
        Phone_No_entry.grid(row=3, column=1, padx=10, sticky=W)

        # Address
        Address_label = Label(class_Student_frame, text="Address:", font=("Times New Roman", 12, "bold"), bg="white")
        Address_label.grid(row=4, column=2, padx=10, pady=10, sticky=W)

        Address_entry = ttk.Entry(class_Student_frame, textvariable=self.var_address, width=20, font=("Times New Roman", 12, "bold"))
        Address_entry.grid(row=4, column=3, padx=10, sticky=W)

        # Teacher Name
        Teacher_Name_label = Label(class_Student_frame, text="Teacher Name:", font=("Times New Roman", 12, "bold"), bg="white")
        Teacher_Name_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)

        Teacher_Name_entry = ttk.Entry(class_Student_frame, textvariable=self.var_teacher, width=20, font=("Times New Roman", 12, "bold"))
        Teacher_Name_entry.grid(row=4, column=1, padx=10, sticky=W)

        # Radio buttons
        self.var_radio = StringVar()  # Use a single StringVar for both radio buttons
        Radiobtn1 = ttk.Radiobutton(class_Student_frame, variable=self.var_radio, text="Take Photo Sample", value="Yes")
        Radiobtn1.grid(row=5, column=0)

        Radiobtn2 = ttk.Radiobutton(class_Student_frame, variable=self.var_radio, text="No Photo Sample", value="No")
        Radiobtn2.grid(row=5, column=1)

        # Button frame
        btn_frame = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=250, width=720, height=40)

        # Save
        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=17, font=("Times New Roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, width=17, text="Update", font=("Times New Roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, width=17, text="Delete", font=("Times New Roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, width=17, text="Reset", font=("Times New Roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # Button frame
        btn_frame1 = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=290, width=720, height=40)

        # Take photo
        Take_photo_btn = Button(btn_frame1, width=34, text="Take photo Sample", font=("Times New Roman", 13, "bold"), bg="blue", fg="white")
        Take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame1, width=34, text="Update photo Sample", font=("Times New Roman", 13, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)

        # Right label frame
        RIGHT_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("Times New Roman", 12, "bold"))
        RIGHT_frame.place(x=770, y=10, width=740, height=580)

        img_right = Image.open(r"C:\Users\Abhishek Sainani\Desktop\images of project\photo.jpg")
        img_right = img_right.resize((550, 130), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(RIGHT_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=740, height=130)

        # Search system
        Search_frame = LabelFrame(RIGHT_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("Times New Roman", 12, "bold"))
        Search_frame.place(x=5, y=135, width=740, height=70)

        # Label of search
        search_label = Label(Search_frame, text="Search by", font=("Times New Roman", 15, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        search_combo = ttk.Combobox(Search_frame, font=("Times New Roman", 12, "bold"), width=17)
        search_combo["values"] = ("Select", "Roll_NO", "Phone_no")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        Search_entry = ttk.Entry(Search_frame, width=20, font=("Times New Roman", 12, "bold"))
        Search_entry.grid(row=0, column=2, padx=10, sticky=W)

        search = Button(Search_frame, width=13, text="Search", font=("Times New Roman", 12, "bold"), bg="blue", fg="white")
        search.grid(row=0, column=3, padx=4)

        showAll = Button(Search_frame, width=13, text="Show All", font=("Times New Roman", 12, "bold"), bg="blue", fg="white")
        showAll.grid(row=0, column=4, padx=4)

        # Table frame
        table_frame = LabelFrame(RIGHT_frame, bd=2, bg="white")
        table_frame.place(x=5, y=210, width=740, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,
                                         columns=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"),
                                         xscrollcommand=scroll_x.set,
                                         yscrollcommand=scroll_y.set
                                         )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Abhi123.", database="face_recognizer",port=330)
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
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
                    self.var_radio.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

### fetch data33========================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Abhi123.", database="face_recognizer",port=330)
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
                conn.commit()
            conn.close()

        #======================= get cursor== or for update
    
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
        self.var_radio.set(data[14])

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()