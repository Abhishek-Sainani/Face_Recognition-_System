from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
class Face_Recognition_System:
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # First image
        img = Image.open(r"C:\Users\Abhishek Sainani\Desktop\images of project\photo.jpg")
        img = img.resize((533, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Second image
        img1 = Image.open(r"C:\Users\Abhishek Sainani\Desktop\images of project\photo.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # Third image
        img2 = Image.open(r"C:\Users\Abhishek Sainani\Desktop\images of project\photo.jpg")
        img2 = img2.resize((533, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=533, height=130)

        # Background image
        img3 = Image.open("background.jpg")
        img3 = img3.resize((1600, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1600, height=710)

        # Title
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Student button
        img4 = Image.open("student-card.png")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="red")
        b1_1.place(x=200, y=300, width=220, height=40)

        # Detect Face
        img5 = Image.open("face2.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="red")
        b1_1.place(x=500, y=300, width=220, height=40)

        # Attendance
        img6 = Image.open("Attendence.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="red")
        b1_1.place(x=800, y=300, width=220, height=40)

        # Help Desk
        img7 = Image.open("help.jpeg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="red")
        b1_1.place(x=1100, y=300, width=220, height=40)

        # Train Data
        img8 = Image.open("traindata.jpg")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b1.place(x=200, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"), bg="blue", fg="red")
        b1_1.place(x=200, y=580, width=220, height=40)

        # Photos
        img9 = Image.open("pho.jpeg")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b1.place(x=500, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"), bg="blue", fg="red")
        b1_1.place(x=500, y=580, width=220, height=40)

        # Developer
        img10 = Image.open("Developer.jpeg")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b1.place(x=800, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Developer", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="red")
        b1_1.place(x=800, y=580, width=220, height=40)

        # Exit
        img11 = Image.open("exit.jpeg")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        b1.place(x=1100, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="red")
        b1_1.place(x=1100, y=580, width=220, height=40)

    def open_img(self):
        os.startfile("data")


        #==========function for windoow

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)  # Ensure the Student class is correctly implemented in student.py

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()