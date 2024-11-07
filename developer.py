from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

# Title
        title_lbl = Label(self.root, text="DEVELOPER", font=("Times New Roman", 35, "bold"), bg="yellow", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Top Image
        img_top = Image.open(r"C:\Users\Abhishek Sainani\Desktop\images of project\photo.jpg")
        img_top = img_top.resize((1530, 720), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)
#FRAME================
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=1000, y=0, width=500, height=690)

        img_top1 = Image.open("myphoto.jpg")
        img_top1 = img_top1.resize((200, 200), Image.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)
        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=300, y=0, width=200, height=200)

#developoer info
        dev_label = Label(main_frame, text="Hello my name is, Abhishek", font=("Times New Roman", 12, "bold"), bg="white")
        dev_label.place(x=0,y=0)

        dev_label = Label(main_frame, text="I am Full Stack Developer", font=("Times New Roman", 12, "bold"), bg="white")
        dev_label.place(x=0,y=40)

        img2 = Image.open("study.png")
        img2 = img2.resize((533, 500), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(main_frame, image=self.photoimg2)
        f_lbl.place(x=0, y=200, width=533, height=500)







if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()