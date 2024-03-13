from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkmacosx import Button
import mysql.connector
import regex as re


class reportClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống quản lý sinh viên")
        self.root.geometry("1200x1000+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # title
        title = Label(
            self.root,
            text="Kết quả học tập",
            font=("goudy old style", 20, "bold"),
            bg="orange",
            fg="#262626",
        ).place(x=10, y=15, width=1180, height=50)

        # search
        self.var_search = StringVar()
        self.var_rid = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks_ob = StringVar()
        self.var_full_marks = StringVar()
        self.var_per = StringVar()

        lbl_search = Label(
            self.root,
            text="Tìm kiếm bằng MSV",
            font=("goudy old style", 20, "bold"),
            bg="white",
        ).place(x=280, y=100)
        # txt_search=Entry(self.root,textvariable=self.var_search,font=("goudy old style",20,),bg="lightyellow").place(x=520,y=100,width=150)
        self.txt_search = Entry(
            self.root,
            textvariable=self.var_search,
            font=("goudy old style", 20, "bold"),
            bg="lightyellow",
        )
        self.txt_search.place(x=520, y=100, width=150)

        btn_search = Button(
            self.root,
            text="Tìm kiếm",
            font=("goudy old style", 15, "bold"),
            bg="#03a9f4",
            fg="white",
            cursor="hand2",
            command=self.search,
        ).place(x=680, y=100, width=100, height=35)
        # btn_clear=Button(self.root,text="Xoá",font=("goudy old style",15,"bold"),bg="gray",fg="white",cursor="hand2").place(x=800,y=100,width=100,height=35)

        # result labels
        # lbl_roll=Label(self.root,text="MSV",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=150,y=230,width=150,height=50)
        # lbl_name=Label(self.root,text="Họ tên",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=300,y=230,width=150,height=50)
        # lbl_course=Label(self.root,text="Môn học",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=450,y=230,width=150,height=50)
        # lbl_marks=Label(self.root,text="Điểm hệ 10",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=600,y=230,width=150,height=50)
        # lbl_full=Label(self.root,text="Điểm chũ",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=750,y=230,width=150,height=50)
        # lbl_per=Label(self.root,text="Điểm hệ 4",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=900,y=230,width=150,height=50)

        # self.roll=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        # self.roll.place(x=150,y=280,width=150,height=50)
        # self.name=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        # self.name.place(x=300,y=280,width=150,height=50)
        # self.course=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        # self.course.place(x=450,y=280,width=150,height=50)
        # self.marks=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        # self.marks.place(x=600,y=280,width=150,height=50)
        # self.full=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        # self.full.place(x=750,y=280,width=150,height=50)
        # self.per=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        # self.per.place(x=900,y=280,width=150,height=50)
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=400, y=200, width=600, height=340)
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.CourseTable = ttk.Treeview(
            self.C_Frame,
            columns=("rid", "roll", "name", "course", "marks_ob", "full_marks", "per"),
            xscrollcommand=scrollx.set,
            yscrollcommand=scrolly.set,
        )
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        self.CourseTable.heading("rid", text="STT")
        self.CourseTable.heading("roll", text="MSV")
        self.CourseTable.heading("name", text="Họ tên")
        self.CourseTable.heading("course", text="Môn")
        self.CourseTable.heading("marks_ob", text="Điểm hệ 10")
        self.CourseTable.heading("full_marks", text="Điểm chữ")
        self.CourseTable.heading("per", text="Điểm hệ 4")
        self.CourseTable["show"] = "headings"
        self.CourseTable.column("rid", width=40)
        self.CourseTable.column("roll", width=40)
        self.CourseTable.column("name", width=80)
        self.CourseTable.column("course", width=100)
        self.CourseTable.column("marks_ob", width=100)
        self.CourseTable.column("full_marks", width=100)
        self.CourseTable.column("per", width=100)
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

        # button delete
        btn_delete = Button(
            self.root,
            text="Loại bỏ",
            font=("goudy old style", 15, "bold"),
            bg="red",
            fg="white",
            cursor="hand2",
            command=self.delete,
        ).place(x=500, y=600, width=150, height=35)

    # =================
    def get_data(self, ev):
        # self.txt_search.config(state='readonly')
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]
        # self.var_rid.set(row[0])
        self.var_roll.set(row[1])
        self.var_name.set(row[2])
        self.var_course.set(row[3])
        self.var_marks_ob.set(row[4])
        self.var_full_marks.set(row[5])
        # self.var_per.delete('1.0',END)
        # self.var_per.insert(END,row[6])

    def search(self):
        con = mysql.connector.connect(
            host="localhost", user="root", passwd="minhhai2806", database="new_schema"
        )
        cur = con.cursor()
        try:
            cur.execute("select * from result where roll=%s", (self.var_search.get(),))
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def show(self):
        con = mysql.connector.connect(
            host="localhost", user="root", passwd="minhhai2806", database="new_schema"
        )
        cur = con.cursor()
        try:
            cur.execute("select * from result")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def clear(self):
        self.show()
        self.var_rid.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks_ob.set("")
        self.var_full_marks.set("")
        self.var_per.set("")

    def delete(self):
        con = mysql.connector.connect(
            host="localhost", user="root", passwd="minhhai2806", database="new_schema"
        )
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Chưa nhập MSV", parent=self.root)
            else:
                cur.execute(
                    "select * from result where roll=%s and course=%s",
                    (self.var_roll.get(), self.var_course.get()),
                )  # Due to tupple we added , at last
                row = cur.fetchone()
                op = messagebox.askyesno(
                    "Confirm", "Bạn muốn xoá?", parent=self.root
                )
                if op == True:
                    cur.execute(
                        "delete from result where roll=%s and course=%s",
                        (self.var_roll.get(), self.var_course.get()),
                    )
                    con.commit()
                    messagebox.showinfo(
                        "Delete", "Xoá thành công", parent=self.root
                    )
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = reportClass(root)
    root.mainloop()
