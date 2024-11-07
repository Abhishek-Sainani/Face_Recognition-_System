from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os 
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        #=================variable=========
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

          # First image
        img = Image.open("scaning.png")
        img = img.resize((800, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

        # Second image
        img1 = Image.open("scaning.png")
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=200)

         # Background image
        img3 = Image.open("background.jpg")
        img3 = img3.resize((1600, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1600, height=710)

        # Title
        title_lbl = Label(bg_img, text="ATTENDANCE", font=("Times New Roman", 35, "bold"), bg="yellow", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=35)

        # Main frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=40, width=1610, height=690)

        
        # Left label frame
        LEFT_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("Times New Roman", 12, "bold"))
        LEFT_frame.place(x=10, y=5, width=750, height=605)

        img_left = Image.open("rasing.png")
        img_left = img_left.resize((550, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(LEFT_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=740, height=130)

        left_inside_frame_frame = Frame(LEFT_frame, bd=2, bg="white")
        left_inside_frame_frame.place(x=0, y=135, width=720, height=370)

#label entery
        #  Attendance id
        attendanceId_label = Label(left_inside_frame_frame, text="AttendanceId:", font=("Times New Roman", 12, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        attendanceID_entry = ttk.Entry(left_inside_frame_frame, width=20,textvariable=self.var_atten_id, font=("Times New Roman", 12, "bold"))
        attendanceID_entry.grid(row=0, column=1, padx=10, sticky=W)
        #rollno

        Roll_no_label = Label(left_inside_frame_frame, text="Roll No:", font=("Times New Roman", 12, "bold"), bg="white")
        Roll_no_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        Roll_no_entry = ttk.Entry(left_inside_frame_frame, width=20,textvariable= self.var_atten_roll, font=("Times New Roman", 12, "bold"))
        Roll_no_entry.grid(row=0, column=3, padx=10, sticky=W)

        #  name
        name_label = Label(left_inside_frame_frame, text="Name:", font=("Times New Roman", 12, "bold"), bg="white")
        name_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        name_entry = ttk.Entry(left_inside_frame_frame, width=20,textvariable=self.var_atten_name, font=("Times New Roman", 12, "bold"))
        name_entry.grid(row=1, column=1, padx=10, sticky=W)

        #Department:

        Department_label = Label(left_inside_frame_frame, text="Department:", font=("Times New Roman", 12, "bold"), bg="white")
        Department_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        Department_entry = ttk.Entry(left_inside_frame_frame, width=20,textvariable=self.var_atten_dep, font=("Times New Roman", 12, "bold"))
        Department_entry.grid(row=1, column=3, padx=10, sticky=W)

         # time
        Time_label = Label(left_inside_frame_frame, text="Time:", font=("Times New Roman", 12, "bold"), bg="white")
        Time_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        Time_entry = ttk.Entry(left_inside_frame_frame, width=20,textvariable=self.var_atten_time, font=("Times New Roman", 12, "bold"))
        Time_entry.grid(row=3, column=1, padx=10, sticky=W)

        #Date

        Date_label = Label(left_inside_frame_frame, text="Date:", font=("Times New Roman", 12, "bold"), bg="white")
        Date_label.grid(row=3, column=2, padx=10, pady=10, sticky=W)

        Date_entry = ttk.Entry(left_inside_frame_frame, width=20,textvariable=self.var_atten_date, font=("Times New Roman", 12, "bold"))
        Date_entry.grid(row=3, column=3, padx=10, sticky=W)
        #attendance status

        class_div_label = Label(left_inside_frame_frame, text="Attendance:", font=("Times New Roman", 12, "bold"), bg="white")
        class_div_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)

        
        div_combo = ttk.Combobox(left_inside_frame_frame, font=("Times New Roman", 12, "bold"), width=17,textvariable=self.var_atten_attendance)
        div_combo["values"] = ("Status", "Present", "Absent",)
        div_combo.current(0)
        div_combo.grid(row=4, column=1, padx=2, pady=10, sticky=W)

         # Button frame
        btn_frame = Frame(left_inside_frame_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=720, height=40)

        # Save
        save_btn = Button(btn_frame, text="Import csv",command=self.importCsv,  width=17, font=("Times New Roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, width=17,  text="Export csv", command=self.exportCsv, font=("Times New Roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, width=17,  text="Update",command=self.update_data, font=("Times New Roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, width=17, text="Reset",command=self.reset_data, font=("Times New Roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        






        # Right label frame
        RIGHT_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("Times New Roman", 12, "bold"))
        RIGHT_frame.place(x=770, y=10, width=740, height=580)


        table_frame = Frame(RIGHT_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=710, height=445)

        #=============scrolll bar table =====

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        #face data=================

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
#import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(
    initialdir=os.getcwd(),  # Use initialdir instead of initial
    title="Open CSV",
    filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),  # Corrected filetypes
    parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
                self.fetchData(mydata)

#export csv 
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(
            initialdir=os.getcwd(),  # Use current working directory
            title="Save CSV File",  # Changed title to Save
            filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),  # Corrected filetypes
            parent=self.root
        )
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("data Export","your data exported to "+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

    # Add this method to your Attendance class
    def update_data(self):
        if self.var_atten_id.get() == "":
            messagebox.showerror("Error", "Please select a record to update", parent=self.root)
            return
        
        # Get the updated data from the entry fields
        updated_id = self.var_atten_id.get()
        updated_roll = self.var_atten_roll.get()
        updated_name = self.var_atten_name.get()
        updated_dep = self.var_atten_dep.get()
        updated_time = self.var_atten_time.get()
        updated_date = self.var_atten_date.get()
        updated_attendance = self.var_atten_attendance.get()

        # Find the index of the record to update
        for index, row in enumerate(mydata):
            if row[0] == updated_id:  # Assuming the first column is the Attendance ID
                mydata[index] = [updated_id, updated_roll, updated_name, updated_dep, updated_time, updated_date, updated_attendance]
                break
        else:
            messagebox.showerror("Error", "Record not found", parent=self.root)
            return

        # Refresh the table to show updated data
        self.fetchData(mydata)
        messagebox.showinfo("Success", "Record updated successfully", parent=self.root)



            
            
    
        

  

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()