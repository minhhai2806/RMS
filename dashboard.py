from tkinter import *
from PIL import Image, ImageTk
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
from tkmacosx import Button
from tkinter import ttk, messagebox
import mysql.connector
import os
import regex as re
import time


class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Tra cứu bảng điểm sinh viên")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # icon
        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")
        # title
        title = Label(
            self.root,
            text="Tra cứu bảng điểm sinh viên",
            padx=10,
            compound=LEFT,
            image=self.logo_dash,
            font=("goudy old style", 20, "bold"),
            bg="#033054",
            fg="white",
        ).place(x=0, y=0, relwidth=1, height=50)
        # Menu
        M_Frame = LabelFrame(
            self.root,
            text="Menu",
            font=("times new roman", 15),
            cursor="hand2",
            bg="white",
        )
        M_Frame.place(x=10, y=70, width=1400, height=60)

        btn_course = Button(
            M_Frame,
            text="Lớp học",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            command=self.add_course,
        ).place(x=20, y=5, width=200, height=40)
        btn_student = Button(
            M_Frame,
            text="Sinh viên",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            command=self.add_student,
        ).place(x=240, y=5, width=200, height=40)
        btn_result = Button(
            M_Frame,
            text="Kết quả",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            command=self.add_result,
        ).place(x=460, y=5, width=200, height=40)
        btn_view = Button(
            M_Frame,
            text="Theo dõi kết quả",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            command=self.add_report,
        ).place(x=680, y=5, width=200, height=40)
        btn_logout = Button(
            M_Frame,
            text="Đăng xuất",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            command=self.logout,
        ).place(x=900, y=5, width=200, height=40)
        btn_exit = Button(
            M_Frame,
            text="Thoát",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            command=self.exit,
        ).place(x=1120, y=5, width=200, height=40)

        # content_window
        self.bg_img = Image.open("images/bg.jpg")
        self.bg_img = self.bg_img.resize((920, 350), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img).place(
            x=400, y=180, width=920, height=350
        )

        # update_details
        self.lbl_course = Label(
            self.root,
            text="Lớp học\n[ 0 ]",
            font=("goudy", 20),
            bd=10,
            relief=RIDGE,
            bg="#e43b06",
            fg="white",
        )
        self.lbl_course.place(x=400, y=530, width=300, height=100)

        self.lbl_student = Label(
            self.root,
            text="Sinh viên\n[ 0 ]",
            font=("goudy", 20),
            bd=10,
            relief=RIDGE,
            bg="#0676ad",
            fg="white",
        )
        self.lbl_student.place(x=710, y=530, width=300, height=100)

        self.lbl_result = Label(
            self.root,
            text="Kết quả\n[ 0 ]",
            font=("goudy", 20),
            bd=10,
            relief=RIDGE,
            bg="#038074",
            fg="white",
        )
        self.lbl_result.place(x=1020, y=530, width=300, height=100)

        # footer
        footer = Label(
            self.root,
            text="Trường Đại học Công nghệ\nLiên hệ: Phòng công tác sinh viên",
            font=(
                "goudy old style",
                12,
            ),
            bg="#262626",
            fg="white",
        ).pack(side=BOTTOM, fill=X)
        self.update_details()

    def update_details(self):
        con = mysql.connector.connect(
            host="localhost", user="root", passwd="minhhai2806", database="new_schema"
        )
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            cr = cur.fetchall()
            self.lbl_course.config(text=f"Lớp học[{str(len(cr))}]")

            cur.execute("Select * from student")
            cr = cur.fetchall()
            self.lbl_student.config(text=f"Sinh viên\n[{str(len(cr))}]")

            cur.execute("Select * from result")
            cr = cur.fetchall()
            self.lbl_result.config(text=f"Kết quả\n[{str(len(cr))}]")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)

    def logout(self):
        op = messagebox.askyesno(
            "Xác nhận lại", "Bạn muốn đăng xuất ?", parent=self.root
        )
        if op == True:
            self.root.destroy()
            os.system("python3 login.py")

    def exit(self):
        op = messagebox.askyesno("Xác nhận lại", "Bạn muốn thoát ?", parent=self.root)
        if op == True:
            self.root.destroy()


if __name__ == "__main__":
    root = Tk()

    obj = RMS(root)

    root.mainloop()
