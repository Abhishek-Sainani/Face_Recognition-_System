from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from main import Face_Recognition_System  # Ensure this import matches your file structure


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Login")

        # Load and display the background image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Abhishek Sainani\Desktop\images of project\photo.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame for login form
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        # Profile icon
        img1 = Image.open("login.png")  # Replace with actual image path
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        # "Get Started" label
        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # Username label and entry
        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 12))
        self.txtuser.place(x=40, y=180, width=270)

        # Password label and entry
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 12), show="*")
        self.txtpass.place(x=40, y=250, width=270)

        # Login button
        loginbtn = Button(frame, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red", command=self.login)
        loginbtn.place(x=110, y=300, width=120, height=35)

        # Register button
        registerbtn = Button(frame, text="New User Register", font=("times new roman", 10, "bold"), bd=3, relief=RIDGE, fg="white", bg="black", activeforeground="white", activebackground="black", command=self.register)
        registerbtn.place(x=15, y=350, width=160)

        # Forgot password button
        forgot_btn = Button(frame, text="Forgot Password", font=("times new roman", 10, "bold"), bd=3, relief=RIDGE, fg="white", bg="black", activeforeground="white", activebackground="black", command=self.forgot_password)
        forgot_btn.place(x=10, y=380, width=160)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "Abhi" and self.txtpass.get() == "Abhi":
            messagebox.showinfo("Success", "Welcome to the Home Page")
            self.open_face_recognition_system()  # Open the main application
        else:
            messagebox.showerror("Invalid", "Invalid username or password")

    def open_face_recognition_system(self):
        self.root.destroy()  # Close the login window
        new_root = Tk()  # Create a new window for the face recognition system
        obj = Face_Recognition_System(new_root)  # Open the face recognition system
        new_root.mainloop()

    def register(self):
        messagebox.showinfo("Register", "Registration functionality not implemented.")

    def forgot_password(self):
        messagebox.showinfo("Forgot Password", "Forgot password functionality not implemented .")

if __name__ == "__main__":
    root = Tk()
    obj = Login_window(root)
    root.mainloop()