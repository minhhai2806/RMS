from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkmacosx import Button
import mysql.connector
import regex as re


class studentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống quản lý sinh viên")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # title
        title = Label(
            self.root,
            text="Hồ sơ sinh viên",
            font=("goudy old style", 20, "bold"),
            bg="#033054",
            fg="white",
        ).place(x=10, y=15, width=1180, height=35)

        # Variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        # self.var_course=StringVar()
        self.var_a_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()

        # widget
        # column1
        lbl_roll = Label(
            self.root, text="MSV", font=("goudy old style", 15, "bold"), bg="white"
        ).place(x=10, y=60)
        lbl_Name = Label(
            self.root, text="Họ tên", font=("goudy old style", 15, "bold"), bg="white"
        ).place(x=10, y=100)
        lbl_Email = Label(
            self.root, text="Email", font=("goudy old style", 15, "bold"), bg="white"
        ).place(x=10, y=140)
        lbl_gender = Label(
            self.root,
            text="Giới tính",
            font=("goudy old style", 15, "bold"),
            bg="white",
        ).place(x=10, y=180)

        lbl_state = Label(
            self.root,
            text="Quận/Huyện",
            font=("goudy old style", 15, "bold"),
            bg="white",
        ).place(x=10, y=220)
        txt_state = Entry(
            self.root,
            textvariable=self.var_state,
            font=("goudy old style", 15, "bold"),
            bg="lightyellow",
        ).place(x=150, y=220, width=150)

        lbl_city = Label(
            self.root, text="Tỉnh/TP", font=("goudy old style", 15, "bold"), bg="white"
        ).place(x=310, y=220)
        txt_city = Entry(
            self.root,
            textvariable=self.var_city,
            font=("goudy old style", 15, "bold"),
            bg="lightyellow",
        ).place(x=380, y=220, width=100)

        lbl_pin = Label(
            self.root, text="Nơi sinh", font=("goudy old style", 15, "bold"), bg="white"
        ).place(x=480, y=220)
        txt_pin = Entry(
            self.root,
            textvariable=self.var_pin,
            font=("goudy old style", 15, "bold"),
            bg="lightyellow",
        ).place(x=560, y=220, width=100)

        lbl_address = Label(
            self.root, text="Địa chỉ", font=("goudy old style", 15, "bold"), bg="white"
        ).place(x=10, y=260)

        # Entry Fields
        self.txt_roll = Entry(
            self.root,
            textvariable=self.var_roll,
            font=("goudy old style", 15, "bold"),
            bg="lightyellow",
        )
        self.txt_roll.place(x=150, y=60, width=200)
        txt_name = Entry(
            self.root,
            textvariable=self.var_name,
            font=("goudy old style", 15, "bold"),
            bg="lightyellow",
        ).place(x=150, y=100, width=200)
        txt_email = Entry(
            self.root,
            textvariable=self.var_email,
            font=("goudy old style", 15, "bold"),
            bg="lightyellow",
        ).place(x=150, y=140, width=200)
        self.txt_gender = ttk.Combobox(
            self.root,
            textvariable=self.var_gender,
            values=("Nam", "Nữ", "Khác"),
            font=("goudy old style", 15, "bold"),
            state="readonly",
            justify=CENTER,
        )
        self.txt_gender.place(x=150, y=180, width=200)
        self.txt_gender.set("Chọn")

        # column2
        lbl_dob = Label(
            self.root,
            text="Ngày sinh",
            font=("goudy old style", 15, "bold"),
            bg="white",
        ).place(x=360, y=60)
        lbl_contact = Label(
            self.root, text="SĐT", font=("goudy old style", 15, "bold"), bg="white"
        ).place(x=360, y=100)
        lbl_admission = Label(
            self.root, text="Lớp", font=("goudy old style", 15, "bold"), bg="white"
        ).place(x=360, y=140)
        # lbl_course=Label(self.root,text="Môn học",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=180)

        # Entry Fields
        # self.course_list=[]
        # function_call to update list
        # self.fetch_course()
        txt_dob = Entry(
            self.root,
            textvariable=self.var_dob,
            font=("goudy old style", 15, "bold"),
            bg="lightyellow",
        ).place(x=480, y=60, width=200)
        txt_contact = Entry(
            self.root,
            textvariable=self.var_contact,
            font=("goudy old style", 15, "bold"),
            bg="lightyellow",
        ).place(x=480, y=100, width=200)
        txt_admission = Entry(
            self.root,
            textvariable=self.var_a_date,
            font=("goudy old style", 15, "bold"),
            bg="lightyellow",
        ).place(x=480, y=140, width=200)
        # self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
        # self.txt_course.place(x=480,y=180,width=200)
        # self.txt_course.set("Chọn")

        # Text address
        self.txt_address = Text(
            self.root, font=("goudy old style", 15, "bold"), bg="lightyellow"
        )
        self.txt_address.place(x=150, y=260, width=540, height=100)

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
        lbl_search_roll = Label(
            self.root, text="MSV", font=("goudy old style", 15, "bold"), bg="white"
        ).place(x=720, y=60)
        txt_roll = Entry(
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
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.CourseTable = ttk.Treeview(
            self.C_Frame,
            columns=(
                "roll",
                "name",
                "email",
                "gender",
                "dob",
                "contact",
                "admission",
                "state",
                "city",
                "pin",
                "address",
            ),
            xscrollcommand=scrollx.set,
            yscrollcommand=scrolly.set,
        )
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        self.CourseTable.heading("roll", text="MSV")
        self.CourseTable.heading("name", text="Họ tên")
        self.CourseTable.heading("email", text="Email")
        self.CourseTable.heading("gender", text="Giới tính")
        self.CourseTable.heading("dob", text="Ngày sinh")
        self.CourseTable.heading("contact", text="SĐT")
        self.CourseTable.heading("admission", text="Lớp")
        # self.CourseTable.heading("course",text="Môn")
        self.CourseTable.heading("state", text="Quận/Huyện")
        self.CourseTable.heading("city", text="Tỉnh/TP")
        self.CourseTable.heading("pin", text="Nơi sinh")
        self.CourseTable.heading("address", text="Địa chỉ")
        self.CourseTable["show"] = "headings"
        self.CourseTable.column("roll", width=100)
        self.CourseTable.column("name", width=100)
        self.CourseTable.column("email", width=100)
        self.CourseTable.column("gender", width=100)
        self.CourseTable.column("dob", width=100)
        self.CourseTable.column("contact", width=100)
        self.CourseTable.column("admission", width=100)
        # self.CourseTable.column("course",width=100)
        self.CourseTable.column("state", width=100)
        self.CourseTable.column("city", width=100)
        self.CourseTable.column("pin", width=100)
        self.CourseTable.column("address", width=200)
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()
        # self.fetch_course()

        #

    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Chọn")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        # self.var_course.set("Chọn")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.txt_address.delete("1.0", END)
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")

    def delete(self):
        con = mysql.connector.connect(
            host="localhost", user="root", passwd="minhhai2806", database="new_schema"
        )
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Chưa điền MSV", parent=self.root)
            else:
                cur.execute(
                    "select * from student where roll=%s", (self.var_roll.get(),)
                )  # Due to tupple we added , at last
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Chưa chọn sinh viên", parent=self.root
                    )
                else:
                    op = messagebox.askyesno(
                        "Confirm", "Bạn muốn loại bỏ", parent=self.root
                    )
                    if op == True:
                        cur.execute(
                            "delete from student where roll=%s", (self.var_roll.get(),)
                        )
                        con.commit()
                        messagebox.showinfo(
                            "Delete", "Loại bỏ thành công", parent=self.root
                        )
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def get_data(self, ev):
        self.txt_roll.config(state="readonly")
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_a_date.set(row[6])
        # self.var_course.set(row[7])
        self.var_state.set(row[7])
        self.var_city.set(row[8])
        self.var_pin.set(row[9])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[10])

    def add(self):
        con = mysql.connector.connect(
            host="localhost", user="root", passwd="minhhai2806", database="new_schema"
        )
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Chưa điền MSV", parent=self.root)
            else:
                cur.execute(
                    "select * from student where roll=%s", (self.var_roll.get(),)
                )  # Due to tupple we added , at last
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "MSV đã tồn tại", parent=self.root)
                else:
                    cur.execute(
                        "Insert into student (roll,name,email,gender,dob,contact,admission,state,city,pin,address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.var_roll.get(),
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_contact.get(),
                            self.var_a_date.get(),
                            # self.var_course.get(),
                            self.var_state.get(),
                            self.var_city.get(),
                            self.var_pin.get(),
                            self.txt_address.get("1.0", END),
                        ),
                    )
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Cập nhật thành công", parent=self.root
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
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Chưa chọn MSV", parent=self.root)
            else:
                cur.execute(
                    "Select * from student where roll=%s", (self.var_roll.get(),)
                )  # Due to tupple we added , at last
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Chọn sinh viên trong danh sách", parent=self.root
                    )
                else:
                    cur.execute(
                        "Update student set name=%s,email=%s,gender=%s,dob=%s,contact=%s,admission=%s,state=%s,city=%s,pin=%s,address=%s where roll=%s",
                        (
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_contact.get(),
                            self.var_a_date.get(),
                            # self.var_course.get(),
                            self.var_state.get(),
                            self.var_city.get(),
                            self.var_pin.get(),
                            self.txt_address.get("1.0", END),
                            self.var_roll.get(),
                        ),
                    )
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Cập nhật thành công", parent=self.root
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
            cur.execute("select * from student")
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
            cur.execute("select * from student where roll=%s", (self.var_search.get(),))
            row = cur.fetchone()
            # print(row)
            if row != None:
                self.CourseTable.delete(*self.CourseTable.get_children())
                self.CourseTable.insert("", END, values=row)
            else:
                messagebox.showerror("Error", "Kết quả không tồn tại", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = studentClass(root)
    root.mainloop()
