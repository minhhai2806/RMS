from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkmacosx import Button
import mysql.connector
import regex as re


class resultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống quản lý sinh viên")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # title
        title = Label(
            self.root,
            text="Nhập điểm",
            font=("goudy old style", 20, "bold"),
            bg="orange",
            fg="#262626",
        ).place(x=10, y=15, width=1180, height=50)

        # widgets
        # variabels
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        # self.var_full_marks=StringVar()
        self.roll_list = []
        self.fetch_roll()

        lbl_select = Label(
            self.root, text="MSV", font=("goudy old style", 20, "bold"), bg="white"
        ).place(x=50, y=100)
        lbl_name = Label(
            self.root, text="Họ tên ", font=("goudy old style", 20, "bold"), bg="white"
        ).place(x=50, y=160)
        lbl_course = Label(
            self.root, text="Môn học", font=("goudy old style", 20, "bold"), bg="white"
        ).place(x=50, y=220)
        lbl_marks_ob = Label(
            self.root, text="Điểm", font=("goudy old style", 20, "bold"), bg="white"
        ).place(x=50, y=280)
        # lbl_full_marks=Label(self.root,text="Full Marks",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=340)

        self.txt_student = ttk.Combobox(
            self.root,
            textvariable=self.var_roll,
            values=self.roll_list,
            font=("goudy old style", 15, "bold"),
            state="readonly",
            justify=CENTER,
        )
        self.txt_student.place(x=280, y=100, width=200)
        self.txt_student.set("Chọn")
        btn_search = Button(
            self.root,
            text="Tìm kiếm",
            font=("goudy old style", 15, "bold"),
            bg="#03a9f4",
            fg="white",
            cursor="hand2",
            command=self.search,
        ).place(x=500, y=100, width=100, height=28)

        txt_name = Entry(
            self.root,
            textvariable=self.var_name,
            font=("goudy old style", 20, "bold"),
            bg="lightyellow",
            state="readonly",
        ).place(x=280, y=160, width=320)
        self.course_list = []
        # function_call to update list
        self.fetch_course()
        # txt_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",20,"bold"),bg="lightyellow",state="readonly").place(x=280,y=220,width=320)
        self.txt_course = ttk.Combobox(
            self.root,
            textvariable=self.var_course,
            values=self.course_list,
            font=("goudy old style", 20, "bold"),
            state="readonly",
            justify=CENTER,
        )
        self.txt_course.place(x=280, y=220, width=200)
        self.txt_course.set("Chọn")

        txt_marks = Entry(
            self.root,
            textvariable=self.var_marks,
            font=("goudy old style", 20, "bold"),
            bg="lightyellow",
        ).place(x=280, y=280, width=320)
        # txt_full_marks=Entry(self.root,textvariable=self.var_full_marks,font=("goudy old style",20,"bold"),bg="lightyellow",state="readonly").place(x=280,y=360,width=320)

        # buttons
        self.btn_add = Button(
            self.root,
            text="Thêm",
            font=("times new roman", 15, "bold"),
            bg="lightgreen",
            activebackground="lightgreen",
            cursor="hand2",
            command=self.add,
        ).place(x=300, y=420, width=120, height=35)
        self.btn_clear = Button(
            self.root,
            text="Xoá",
            font=("times new roman", 15, "bold"),
            bg="lightgray",
            activebackground="lightgray",
            cursor="hand2",
            command=self.clear,
        ).place(x=430, y=420, width=120, height=35)

        # image
        self.bg_img = Image.open("images/result.png")
        self.bg_img = self.bg_img.resize((500, 300), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img).place(x=630, y=100)

    # -------------
    def fetch_roll(self):
        con = mysql.connector.connect(
            host="localhost", user="root", passwd="minhhai2806", database="new_schema"
        )
        cur = con.cursor()
        try:
            cur.execute("select roll from student")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.roll_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def fetch_course(self):
        con = mysql.connector.connect(
            host="localhost", user="root", passwd="minhhai2806", database="new_schema"
        )
        cur = con.cursor()
        try:
            cur.execute("select name from course")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def search(self):
        con = mysql.connector.connect(
            host="localhost", user="root", passwd="minhhai2806", database="new_schema"
        )
        cur = con.cursor()
        try:
            cur.execute(
                "select name from student where roll=%s", (self.var_roll.get(),)
            )
            row = cur.fetchone()
            if row != None:
                self.var_name.set(row[0])
                # self.var_course.set(row[1])
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def add(self):
        con = mysql.connector.connect(
            host="localhost", user="root", passwd="minhhai2806", database="new_schema"
        )
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Chưa chọn MSV", parent=self.root)
            else:
                cur.execute(
                    "select * from result where roll=%s and course=%s",
                    (self.var_roll.get(), self.var_course.get()),
                )
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", "Kết quả đã tồn tại", parent=self.root
                    )
                else:
                    if (float(self.var_marks.get())) >= 9 and (
                        float(self.var_marks.get())
                    ) <= 10:
                        full = "A+"
                        per = 4.0
                    # per=(int(self.var_marks.get())*100)/int(self.var_full_marks.get())
                    elif (float(self.var_marks.get())) < 9 and (
                        float(self.var_marks.get())
                    ) >= 8.5:
                        full = "A"
                        per = 3.7
                    elif (float(self.var_marks.get())) < 8.5 and (
                        float(self.var_marks.get())
                    ) >= 8:
                        full = "B+"
                        per = 3.5
                    elif (float(self.var_marks.get())) < 8 and (
                        float(self.var_marks.get())
                    ) >= 7:
                        full = "B"
                        per = 3.0
                    elif (float(self.var_marks.get())) < 7 and (
                        float(self.var_marks.get())
                    ) >= 6.5:
                        full = "C+"
                        per = 2.5
                    elif (float(self.var_marks.get())) < 6.5 and (
                        float(self.var_marks.get())
                    ) >= 5.5:
                        full = "C"
                        per = 2
                    elif (float(self.var_marks.get())) < 5.5 and (
                        float(self.var_marks.get())
                    ) >= 5:
                        full = "D+"
                        per = 1.5
                    elif (float(self.var_marks.get())) < 5 and (
                        float(self.var_marks.get())
                    ) >= 4:
                        full = "D"
                        per = 1
                    else:
                        full = "F"
                        per = 0
                    cur.execute(
                        "Insert into result(roll,name,course,marks_ob,full_marks,per) values(%s,%s,%s,%s,%s,%s)",
                        (
                            self.var_roll.get(),
                            self.var_name.get(),
                            self.var_course.get(),
                            self.var_marks.get(),
                            str(full),
                            str(per),
                        ),
                    )
                    con.commit()
                    messagebox.showinfo("Success", "Thành công", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def clear(self):
        self.var_roll.set("Chọn"),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_marks.set(""),
        # self.var_full_marks.set(""),


if __name__ == "__main__":
    root = Tk()
    obj = resultClass(root)
    root.mainloop()
