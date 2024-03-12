# Register Page
from tkinter import *
from tkinter import ttk, messagebox
from turtle import width
from PIL import Image, ImageTk
import os
from tkmacosx import Button
import regex as re
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Cửa số đăng ký")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        # ===Bg Image===
        self.bg = ImageTk.PhotoImage(file="images/login.jpg")
        bg = Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)
        # ===LEFT image===
        self.left = ImageTk.PhotoImage(file="images/login.jpg")
        left = Label(self.root, image=self.left).place(
            x=80, y=100, width=400, height=500
        )

        # ===Register frame ====
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=550)
        title = Label(
            frame1,
            text="ĐĂNG KÝ",
            font=("times new roman", 20, "bold"),
            bg="white",
            fg="green",
        ).place(x=50, y=30)
        # ----------------Row1
        self.var_fname = StringVar()
        f_name = Label(
            frame1,
            text="Họ",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="gray",
        ).place(x=50, y=100)
        self.txt_fname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_fname.place(x=50, y=130, width=250)

        l_name = Label(
            frame1,
            text="Tên",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="gray",
        ).place(x=370, y=100)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)
        # -------------Row2
        contact = Label(
            frame1,
            text="SĐT",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="gray",
        ).place(x=50, y=170)
        self.txt_contact = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=200, width=250)
        # -----------------Row3
        email = Label(
            frame1,
            text="Email",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="gray",
        ).place(x=370, y=170)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)

        # ----------------Row4
        question = Label(
            frame1,
            text="Câu hỏi bảo mật",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="gray",
        ).place(x=50, y=240)
        self.cmb_quest = ttk.Combobox(
            frame1, font=("times new roman", 13), state="readonly", justify=CENTER
        )
        self.cmb_quest["values"] = (
            "Chọn",
            "Vật nuôi yêu thích",
            "Nơi sinh",
            "Môn thể thao bạn thích",
        )
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)

        answer = Label(
            frame1,
            text="Câu trả lời",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="gray",
        ).place(x=370, y=240)
        self.txt_answer = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=370, y=270, width=250)

        # -------Row5
        password = Label(
            frame1,
            text="Mật khẩu",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="gray",
        ).place(x=50, y=310)
        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_password.place(x=50, y=340, width=250)

        cpassword = Label(
            frame1,
            text="Xác nhận mật khẩu",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="gray",
        ).place(x=370, y=310)
        self.txt_cpassword = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_cpassword.place(x=370, y=340, width=250)

        UserType = Label(
            frame1,
            text="Quyền hạn",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="gray",
        ).place(x=180, y=380)
        self.txt_UserType = ttk.Combobox(
            frame1, font=("times new roman", 13), state="readonly", justify=CENTER
        )
        self.txt_UserType["values"] = ("Chọn", "Sinh viên", "Giảng viên")
        self.txt_UserType.place(x=270, y=380, width=100)
        self.txt_UserType.current(0)

        # -------Terms-----
        self.var_chk = IntVar()
        chk = Checkbutton(
            frame1,
            text="Tôi đồng ý với các điều khoản và điều kiện",
            variable=self.var_chk,
            onvalue=1,
            offvalue=0,
            font=("times new roman", 12),
            bg="white",
        ).place(x=50, y=430)

        self.btn_img = Image.open("images/register.png")
        self.btn_img = self.btn_img.resize((200, 100), Image.LANCZOS)
        self.btn_img = ImageTk.PhotoImage(self.btn_img)

        btn_register = Button(
            frame1, image=self.btn_img, bd=0, cursor="hand2", command=self.register_data
        ).place(x=50, y=470)
        btn_login = Button(
            self.root,
            text="Đăng nhập",
            command=self.login_window,
            font=("times new roman", 20, "bold"),
            fg="white",
            bg="blue",
        ).place(x=280, y=580)

    def login_window(self):
        self.root.destroy()
        os.system("python3 login.py")

    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.cmb_quest.current(0)
        self.txt_UserType.current(0)

    # Register Function
    def register_data(self):
        if (
            self.txt_fname.get() == ""
            or self.txt_contact.get() == ""
            or self.txt_email.get() == ""
            or self.cmb_quest.get() == "Select"
            or self.txt_answer.get() == ""
            or self.txt_password.get() == ""
            or self.txt_cpassword.get() == ""
            or self.txt_UserType.get() == "Select"
        ):
            messagebox.showerror("Error", "Chưa diền đủ thông tin", parent=self.root)
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("Error", "Mật khẩu chưa trùng khớp", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror(
                "Error", "Chưa đồng ý điều khoản và điều kiện", parent=self.root
            )
        else:
            try:

                fn = 0
                ln = 0
                # Validation for first and last name
                for i in self.txt_fname.get():
                    if i.isupper() or i.islower():
                        fn += 1
                for i in self.txt_lname.get():
                    if i.isupper() or i.islower():
                        ln += 1
                if (fn == len(self.txt_fname.get())) and (
                    ln == len(self.txt_lname.get())
                ):

                    # Validation for contact number
                    s = 0
                    for i in self.txt_contact.get():
                        if i.isdigit():
                            s += 1
                    if s == 10:

                        # Validation for Email
                        k = self.txt_email.get()[-10:-1]
                        j = k + "m"
                        if (j == "@gmail.com") and len(self.txt_email.get()) >= 12:

                            # Validation for Password
                            l, u, p, d = 0, 0, 0, 0
                            if len(self.txt_password.get()) >= 8:
                                for i in self.txt_password.get():
                                    if i.islower():
                                        l += 1

                                    elif i.isupper():
                                        u += 1
                                    elif i.isdigit():
                                        d += 1
                                    elif (
                                        i == "@"
                                        or i == "&"
                                        or i == "#"
                                        or i == "!"
                                        or i == "_"
                                    ):
                                        p += 1
                                if l >= 1 and u >= 1 and d >= 1 and p >= 1:
                                    # connection with database
                                    con = mysql.connector.connect(
                                        host="localhost",
                                        user="root",
                                        passwd="minhhai2806",
                                        database="new_schema",
                                    )
                                    cur = con.cursor()
                                    cur.execute(
                                        "select * from AllUsers where email=%s",
                                        (self.txt_email.get(),),
                                    )
                                    row = cur.fetchone()

                                    if row != None:
                                        messagebox.showerror(
                                            "Error",
                                            "Email đã tồn tại",
                                            parent=self.root,
                                        )
                                    else:
                                        cur.execute(
                                            "insert into AllUsers (f_name,l_name, contact, email, question, answer, password,u_name) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                                            (
                                                self.txt_fname.get(),
                                                self.txt_lname.get(),
                                                self.txt_contact.get(),
                                                self.txt_email.get(),
                                                self.cmb_quest.get(),
                                                self.txt_answer.get(),
                                                self.txt_password.get(),
                                                self.txt_UserType.get(),
                                            ),
                                        )
                                        con.commit()
                                        con.close()
                                        messagebox.showinfo(
                                            "Thành công",
                                            "Đăng ký thành công",
                                            parent=self.root,
                                        )
                                        self.clear()
                                        self.login_window()

                                else:
                                    messagebox.showerror(
                                        "Error",
                                        "Mật khẩu tối thiểu 8 ký tự bao gồm ít nhất 1 ký tự thường, 1 ký tự in hoa, 1 số và 1 ký tự đặc biệt '@','&','#','!','_'",
                                        parent=self.root,
                                    )
                            else:
                                messagebox.showerror(
                                    "Error",
                                    "Mật khẩu tối thiểu 8 ký tự bao gồm ít nhất 1 ký tự thường, 1 ký tự in hoa, 1 số và 1 ký tự đặc biệt '@','&','#','!','_'",
                                    parent=self.root,
                                )

                        else:
                            messagebox.showerror("Error", "Chưa nhập email")
                    else:
                        messagebox.showerror("Error", "Chưa nhập SĐT")
                else:
                    messagebox.showerror("Error", "Chưa nhập đúng tên")

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to:{str(es)}", parent=self.root
                )


root = Tk()
obj = Register(root)
root.mainloop()
