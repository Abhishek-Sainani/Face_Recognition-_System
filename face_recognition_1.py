from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
import cv2
import numpy as np
from datetime import datetime


class Face_Recognition1:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("Times New Roman", 35, "bold"), bg="yellow", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # 1ST IMAGE
        img_top = Image.open(r"robotic.png")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        # SECOND IMAGE
        img_bottom = Image.open("robotic2.png")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        # Button
        b1_1 = Button(f_lbl, text="DETECT FACE", command=self.face_recog, cursor="hand2", font=("times new roman", 18, "bold"), bg="green", fg="white")
        b1_1.place(x=385, y=600, width=200, height=40)

        # Set to track attendance
        self.attendance_set = set()

    def mark_attendance(self, student_id, roll, name, department):
        if student_id not in self.attendance_set:  # Check if already marked
            with open("abhishek.csv", "a", newline="") as f:  # Open in append mode
                now = datetime.now()
                date_str = now.strftime("%d/%m/%Y")
                time_str = now.strftime("%H:%M:%S")
                f.write(f"{student_id},{roll},{name},{department},{time_str},{date_str},Present\n")
                print(f"Attendance marked for {name} (ID: {student_id})")
                self.attendance_set.add(student_id)  # Add to the set
        else:
            print(f"Attendance already marked for ID: {student_id}")
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                # Database connection
                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="Abhi123.",
                        database="face_recognizer",
                        port=330  # Default MySQL port
                    )
                    my_cursor = conn.cursor()
                    print(f"Connected to database, Student ID: {id}")

                    # Fetch details
                    my_cursor.execute("SELECT Name, Roll, Dep FROM student WHERE Student_id=%s", (id,))
                    result = my_cursor.fetchone()
                    if result:
                        name, roll, department = result
                        print(f"Name: {name}, Roll: {roll}, Department: {department}")

                        if confidence > 20:
                            self.mark_attendance (id, roll, name, department)  # Save attendance
                            cv2.putText(img, f"Roll: {roll}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                            cv2.putText(img, f"Name: {name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                            cv2.putText(img, f"Department: {department}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        else:
                            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                            cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                except mysql.connector.Error as err:
                    print(f"Database Error: {err}")
                    return
                finally:
                    if conn:
                        conn.close()
                        print("Connection closed")

        def recognize(img, clf, faceCascade):
            draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        try:
            while True:
                ret, img = video_cap.read()
                if not ret:
                    print("Failed to capture image from camera")
                    break

                img = recognize(img, clf, faceCascade)
                cv2.imshow("Welcome to Face Recognition", img)

                if cv2.waitKey(1) == 13:  # Press 'Enter' to exit
                    break
        except Exception as e:
            print(f"Error during face recognition: {e}")
        finally:
            video_cap.release()
            cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition1(root)
    root.mainloop()