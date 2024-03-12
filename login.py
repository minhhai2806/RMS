from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
import mysql.connector
import os
from tkmacosx import Button
import regex as re


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Đăng nhập hệ thống")
        self.root.geometry("1400x700+0+0")
        # ====BG IMage=====
        self.bg = ImageTk.PhotoImage(file="images/login.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1
        )

        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=500, y=100, height=550, width=500)

        # Login title
        title = Label(
            Frame_login,
            text="ĐĂNG NHẬP",
            font=("Times New Roman", 25, "bold"),
            fg="navy blue",
            bg="white",
        ).place(x=200, y=20)

        # Username and password lable
        lbl_user = Label(
            Frame_login,
            text="Tên đăng nhập",
            font=("Times New Roman", 15, "bold"),
            fg="black",
            bg="light gray",
        ).place(x=45, y=140)
        self.txt_user = Entry(Frame_login, font=("times new roman", 15), bg="white")
        self.txt_user.place(x=45, y=170, width=400, height=35)

        lbl_pass = Label(
            Frame_login,
            text="Mật khẩu",
            font=("Times New Roman", 15, "bold"),
            fg="black",
            bg="light gray",
        ).place(x=45, y=240)
        self.txt_pass = Entry(Frame_login, font=("times new roman", 15), bg="white")
        self.txt_pass.place(x=45, y=270, width=400, height=35)

        forget = Button(
            Frame_login,
            text="Quên mật khẩu?",
            cursor="hand2",
            command=self.forget_window,
            bg="white",
            fg="blue",
            font=("times new roman", 15, "bold"),
        ).place(x=180, y=320)

        # Buttons
        signup = Button(
            Frame_login,
            text="Đăng ký",
            cursor="hand2",
            bg="blue",
            fg="white",
            font=("times new roman", 12, "bold"),
            command=self.register_window,
        ).place(x=220, y=480, height=40)

        login = Button(
            Frame_login,
            text="Đăng nhập",
            cursor="hand2",
            bg="navy blue",
            fg="white",
            font=("times new roman", 20, "bold"),
            command=self.login_function,
        ).place(x=210, y=370, width=100, height=50)

        lbl_create = Label(
            Frame_login,
            text="Tạo tài khoản?",
            font=("Times New Roman", 15, "bold"),
            fg="black",
            bg="light gray",
        ).place(x=210, y=450)

        # Checkbuttons
        UserType = Label(
            Frame_login,
            text="Quyền hạn: ",
            font=("times new roman", 15, "bold"),
            bg="light gray",
            fg="black",
        ).place(x=45, y=85)
        self.txt_UserType = ttk.Combobox(
            Frame_login, font=("times new roman", 13), state="readonly", justify=CENTER
        )
        self.txt_UserType["values"] = ("Chọn", "Sinh viên", "Giảng viên")
        self.txt_UserType.place(x=120, y=85, width=120, height=30)
        self.txt_UserType.current(0)

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_passwd.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_pass.delete(0, END)
        self.txt_user.delete(0, END)

    def forget_passwd(self):
        if (
            self.cmb_quest.get() == "Chọn"
            or self.txt_answer.get() == ""
            or self.txt_new_passwd.get() == ""
        ):
            messagebox.showerror("Error", "Chưa điền đủ thông tin", parent=self.root2)
        else:
            try:
                con = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="minhhai2806",
                    database="new_schema",
                )
                cur = con.cursor()
                cur = con.cursor()
                cur.execute(
                    "Select * from AllUsers where email=%s and question=%s and answer=%s",
                    (self.txt_user.get(), self.cmb_quest.get(), self.txt_answer.get()),
                )
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error",
                        "Chưa chọn đúng câu hỏi bảo mật và câu trả lời",
                        parent=self.root2,
                    )

                else:  # Coding for Password Pattern
                    l, u, p, d = 0, 0, 0, 0
                    if len(self.txt_new_passwd.get()) >= 8:
                        for i in self.txt_new_passwd.get():
                            if i.islower():
                                l += 1

                            elif i.isupper():
                                u += 1
                            elif i.isdigit():
                                d += 1
                            elif (
                                i == "@" or i == "&" or i == "#" or i == "!" or i == "_"
                            ):
                                p += 1
                        if l >= 1 and u >= 1 and d >= 1 and p >= 1:

                            cur.execute(
                                "update AllUsers set password=%s where email=%s ",
                                (self.txt_new_passwd.get(), self.txt_user.get()),
                            )
                            con.commit()
                            con.close()
                            messagebox.showinfo(
                                "Success",
                                "Mật khẩu đã được đổi, mời đăng nhập",
                                parent=self.root2,
                            )
                            self.reset()
                            self.root2.destroy()
                        else:
                            messagebox.showerror(
                                "Error",
                                "Mật khẩu tối thiểu 8 ký tự bao gồm ít nhất 1 ký tự thường, 1 ký tự in hoa, 1 số và 1 ký tự đặc biệt '@','&','#','!','_'",
                                parent=self.root2,
                            )
                    else:
                        messagebox.showerror(
                            "Error",
                            "Mật khẩu tối thiểu 8 ký tự bao gồm ít nhất 1 ký tự thường, 1 ký tự in hoa, 1 số và 1 ký tự đặc biệt '@','&','#','!','_'",
                            parent=self.root2,
                        )

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error Due to: {str(es)}", parent=self.root
                )

    # Forget Password Window
    def forget_window(self):
        if self.txt_user.get() == "":
            messagebox.showerror("Error", "Vui lòng chọn email", parent=self.root)
        else:
            try:
                con = con = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="minhhai2806",
                    database="new_schema",
                )
                cur = con.cursor()
                cur = con.cursor()
                cur.execute(
                    "Select * from AllUsers where email=%s", (self.txt_user.get(),)
                )  # Selecting AllUsers Database i.e.(Those Who Sign Up)
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Vui lòng nhập email đã đăng ký ", parent=self.root
                    )

                else:
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Quên mật khẩu")
                    self.root2.geometry("400x400+500+150")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    # Title for Forget Interface
                    title = Label(
                        self.root2,
                        text="Quên mật khẩu",
                        font=("Times New Roman", 25),
                        fg="red",
                        bg="white",
                    ).place(x=0, relwidth=1)
                    # Contents in Forget Password Page
                    question = Label(
                        self.root2,
                        text="Câu hỏi bảo mật",
                        font=("times new roman", 15, "bold"),
                        bg="white",
                        fg="gray",
                    ).place(x=50, y=100)
                    self.cmb_quest = ttk.Combobox(
                        self.root2,
                        font=("times new roman", 13),
                        state="readonly",
                        justify=CENTER,
                    )
                    self.cmb_quest["values"] = (
                        "Chọn",
                        "Vật nuôi yêu thích",
                        "Nơi sinh",
                        "Môn thể thao bạn thích",
                    )
                    self.cmb_quest.place(x=50, y=130, width=250)
                    self.cmb_quest.current(0)

                    answer = Label(
                        self.root2,
                        text="Câu trả lời",
                        font=("times new roman", 15, "bold"),
                        bg="white",
                        fg="gray",
                    ).place(x=50, y=180)
                    self.txt_answer = Entry(
                        self.root2, font=("times new roman", 15), bg="lightgray"
                    )
                    self.txt_answer.place(x=50, y=210, width=250)

                    new_passwd = Label(
                        self.root2,
                        text="Mật khẩu mới",
                        font=("times new roman", 15, "bold"),
                        bg="white",
                        fg="gray",
                    ).place(x=50, y=260)
                    self.txt_new_passwd = Entry(
                        self.root2, font=("times new roman", 15), bg="lightgray"
                    )
                    self.txt_new_passwd.place(x=50, y=290, width=250)

                    btn_change_passwd = Button(
                        self.root2,
                        text="Đổi mật khẩu",
                        command=self.forget_passwd,
                        bg="Green",
                        fg="White",
                        font=("times new roman", 15, "bold"),
                    ).place(x=90, y=340)

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error Due to: {str(es)}", parent=self.root
                )

    # By clicking on Sign-Up button going directly on sign-up page by destroying login page
    def register_window(self):
        self.root.destroy()
        import Register

    # Function for Login Part
    def login_function(self):
        if (
            self.txt_pass.get() == ""
            or self.txt_user.get() == ""
            or self.txt_UserType.get() == "Chọn"
        ):
            messagebox.showerror("Error", "Chưa điền thông tin", parent=self.root)

        else:
            try:
                con = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="minhhai2806",
                    database="new_schema",
                )
                cur = con.cursor()
                cur = con.cursor()
                cur.execute(
                    "Select * from AllUsers where email=%s and password=%s and u_name=%s ",
                    (self.txt_user.get(), self.txt_pass.get(), self.txt_UserType.get()),
                )
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error",
                        "Nhập sai thông tin tài khoản, mật khẩu, quyền",
                        parent=self.root,
                    )

                else:
                    if self.txt_UserType.get() == "Sinh viên":
                        messagebox.showinfo(
                            "Thành công",
                            f"Chào mừng :- {self.txt_user.get()}",
                            parent=self.root,
                        )
                        self.root.destroy()
                        os.system("python3 dashboardStudent.py")
                    else:
                        messagebox.showinfo(
                            "Thành công",
                            f"Chào mừng :- {self.txt_user.get()}",
                            parent=self.root,
                        )
                        self.root.destroy()
                        os.system("python3 dashboard.py")
                    con.close()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error Due to: {str(es)}", parent=self.root
                )


root = Tk()
obj = Login(root)
root.mainloop()
