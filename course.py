from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkmacosx import Button
import mysql.connector
import regex as re


class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ Thống Quản Lý Điểm Sinh Viên")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # title
        title = Label(
            self.root,
            text="Quản lý lớp học",
            font=("goudy old style", 20, "bold"),
            bg="#033054",
            fg="white",
        ).place(x=10, y=15, width=1180, height=35)

        # Variables
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()

        # widget
        lbl_courseName = Label(
            self.root,
            text="Tên môn học",
            font=("goudy old style", 15, "bold"),
            bg="white",
        ).place(x=10, y=60)
        lbl_duration = Label(
            self.root,
            text="Số tín chỉ",
            font=("goudy old style", 15, "bold"),
            bg="white",
        ).place(x=10, y=100)
        lbl_charges = Label(
            self.root,
            text="Giảng viên",
            font=("goudy old style", 15, "bold"),
            bg="white",
        ).place(x=10, y=140)
        lbl_description = Label(
            self.root,
            text="Thông tin",
            font=("goudy old style", 15, "bold"),
            bg="white",
        ).place(x=10, y=180)

        # Entry Fields

        self.txt_lbl_courseName = Entry(
            self.root,
            textvariable=self.var_course,
            font=("goudy old style", 15, "bold"),
            bg="lightyellow",
        )
        self.txt_lbl_courseName.place(x=150, y=60, width=200)
        txt_lbl_duration = Entry(
            self.root,
            textvariable=self.var_duration,
            font=("goudy old style", 15, "bold"),
            bg="lightyellow",
        ).place(x=150, y=100, width=200)
        txt_lbl_charges = Entry(
            self.root,
            textvariable=self.var_charges,
            font=("goudy old style", 15, "bold"),
            bg="lightyellow",
        ).place(x=150, y=140, width=200)
        self.txt_description = Text(
            self.root, font=("goudy old style", 15, "bold"), bg="lightyellow"
        )
        self.txt_description.place(x=150, y=180, width=500, height=100)

        # Button
        self.btn_add = Button(
            self.root,
            text="Lưu",
            font=("goudy old style", 15, "bold"),
            bg="#2196f3",
            fg="white",
            cursor="hand2",
            command=self.add,
        )
        self.btn_add.place(x=150, y=400, width=110, height=40)
        self.btn_update = Button(
            self.root,
            text="Cập nhật",
            font=("goudy old style", 15, "bold"),
            bg="#4caf50",
            fg="white",
            cursor="hand2",
            command=self.update,
        )
        self.btn_update.place(x=270, y=400, width=110, height=40)
        self.btn_delete = Button(
            self.root,
            text="Loại bỏ",
            font=("goudy old style", 15, "bold"),
            bg="#f44336",
            fg="white",
            cursor="hand2",
            command=self.delete,
        )
        self.btn_delete.place(x=390, y=400, width=110, height=40)
        self.btn_clear = Button(
            self.root,
            text="Xoá",
            font=("goudy old style", 15, "bold"),
            bg="#2196f3",
            fg="white",
            cursor="hand2",
            command=self.clear,
        )
        self.btn_clear.place(x=510, y=400, width=110, height=40)

        # Search Panel
        self.var_search = StringVar()
        lbl_search_courseName = Label(
            self.root,
            text="Tên môn học",
            font=("goudy old style", 15, "bold"),
            bg="white",
        ).place(x=720, y=60)
        txt_lbl_courseName = Entry(
            self.root,
            textvariable=self.var_search,
            font=("goudy old style", 15, "bold"),
            bg="lightyellow",
        ).place(x=870, y=60, width=180)
        btn_search = Button(
            self.root,
            text="Tìm kiếm",
            font=("goudy old style", 15, "bold"),
            bg="#03a9f4",
            fg="white",
            cursor="hand2",
            command=self.search,
        ).place(x=1070, y=60, width=120, height=28)

        # content
        # scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        # scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)

        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.CourseTable = ttk.Treeview(
            self.C_Frame,
            columns=("cid", "name", "duration", "charges", "description"),
            xscrollcommand=scrollx.set,
            yscrollcommand=scrolly.set,
        )
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        self.CourseTable.heading("cid", text="Mã môn")
        self.CourseTable.heading("name", text="Tên")
        self.CourseTable.heading("duration", text="Số tín ")
        self.CourseTable.heading("charges", text="Giảng viên")
        self.CourseTable.heading("description", text="Thông tin")
        self.CourseTable["show"] = "headings"
        self.CourseTable.column("cid", width=50)
        self.CourseTable.column("name", width=50)
        self.CourseTable.column("duration", width=50)
        self.CourseTable.column("charges", width=170)
        self.CourseTable.column("description", width=150)
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

        #

    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete("1.0", END)
        self.txt_lbl_courseName.config(state=NORMAL)

    def delete(self):
        con = mysql.connector.connect(
            host="localhost", user="root", passwd="minhhai2806", database="new_schema"
        )
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror(
                    "Error", "Course name should be required", parent=self.root
                )
            else:
                cur.execute(
                    "select * from course where name=%s", (self.var_course.get(),)
                )  # Due to tupple we added , at last
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error",
                        "Please select course from the list first",
                        parent=self.root,
                    )
                else:
                    op = messagebox.askyesno(
                        "Confirm", "Do you want to delete?", parent=self.root
                    )
                    if op == True:
                        cur.execute(
                            "delete from course where name=%s", (self.var_course.get(),)
                        )
                        con.commit()
                        messagebox.showinfo(
                            "Delete", "Course delete successfully", parent=self.root
                        )
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def get_data(self, ev):
        self.txt_lbl_courseName.config(state="readonly")
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]

        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_description.delete("1.0", END)
        self.txt_description.insert(END, row[4])

    def add(self):
        con = mysql.connector.connect(
            host="localhost", user="root", passwd="minhhai2806", database="new_schema"
        )
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror(
                    "Error", "Course name should be required", parent=self.root
                )
            else:
                cur.execute(
                    "select * from course where name=%s", (self.var_course.get(),)
                )  # Due to tupple we added , at last
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", "Course name already present", parent=self.root
                    )
                else:
                    cur.execute(
                        "Insert into course (name,duration,charges,description) values(%s,%s,%s,%s)",
                        (
                            self.var_course.get(),
                            self.var_duration.get(),
                            self.var_charges.get(),
                            self.txt_description.get("1.0", END),
                        ),
                    )
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Course Update Successfully", parent=self.root
                    )
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def update(self):
        con = mysql.connector.connect(
            host="localhost", user="root", passwd="minhhai2806", database="new_schema"
        )
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror(
                    "Error", "Course name should be required", parent=self.root
                )
            else:
                cur.execute(
                    "Select * from course where name=%s", (self.var_course.get(),)
                )  # Due to tupple we added , at last
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Select Course from list", parent=self.root
                    )
                else:
                    cur.execute(
                        "Update course set duration=%s,charges=%s,description=%s where name=%s",
                        (
                            self.var_duration.get(),
                            self.var_charges.get(),
                            self.txt_description.get("1.0", END),
                            self.var_course.get(),
                        ),
                    )
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Course Added Successfully", parent=self.root
                    )
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def show(self):
        con = mysql.connector.connect(
            host="localhost", user="root", passwd="minhhai2806", database="new_schema"
        )
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def search(self):
        con = mysql.connector.connect(
            host="localhost", user="root", passwd="minhhai2806", database="new_schema"
        )
        cur = con.cursor()
        try:
            cur.execute(
                f"select * from course where name LIKE '%{self.var_search.get()}%'"
            )
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()
