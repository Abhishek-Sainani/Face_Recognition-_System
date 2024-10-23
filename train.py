from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("Times New Roman", 35, "bold"), bg="yellow", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Top Image
        img_top = Image.open(r"C:\Users\Abhishek Sainani\Desktop\images of project\photo.jpg")
        img_top = img_top.resize((1530, 325), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)

        # Train Data Button
        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("times new roman", 30, "bold"), bg="blue", fg="red")
        b1_1.place(x=0, y=380, width=1530, height=60)

        # Bottom Image
        img_bottom = Image.open(r"C:\Users\Abhishek Sainani\Desktop\images of project\photo.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
        data_dir = "data"
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "Data directory not found!", parent=self.root)
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []

        for image in path:
            try:
                img = Image.open(image).convert('L')  # Convert to grayscale
                imageNP = np.array(img, 'uint8')
                id = int(os.path.split(image)[1].split('.')[1])  # Corrected index to 1

                faces.append(imageNP)
                ids.append(id)
                cv2.imshow("Training", imageNP)
                if cv2.waitKey(1) == 13:  # Break on Enter key
                    break
            except Exception as e:
                print(f"Error processing image {image}: {e}")

        if len(faces) == 0:
            messagebox.showerror("Error", "No faces found for training!", parent=self.root)
            return

        ids = np.array(ids)

        # Train the classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training dataset completed!!")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()