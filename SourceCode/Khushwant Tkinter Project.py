from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title('Noise Pollution Tracker')
        self.root.geometry('925x500+300+200')
        self.root.configure(bg="#fff")
        self.icon_email = PhotoImage(file="C:/Users/DELL/Downloads/email2_icon.png")
        self.icon_user = PhotoImage(file="C:/Users/DELL/Downloads/user_icon.png")
        self.icon_lock = PhotoImage(file="C:/Users/DELL/Downloads/lock3_icon.png")
        self.left_image = PhotoImage(file="C:/Users/DELL/Downloads/leftside.png")

        self.root.resizable(0, 0)
        self.users = {}
        self.welcome_page()

    def welcome_page(self):
        self.clear_page()

        welcome_bg = Image.open("C:/Users/DELL/Downloads/welcome_background.jpg")
        welcome_bg = welcome_bg.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        welcome_bg_photo = ImageTk.PhotoImage(welcome_bg)

        canvas = Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight(), highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=welcome_bg_photo, anchor="nw")
        self.welcome_bg_photo = welcome_bg_photo

        overlay = Frame(self.root, bg="white", bd=0)
        overlay.place(relx=0.5, rely=0.5, anchor="center")

        content_frame = Frame(overlay, bg="white", padx=40, pady=40)
        content_frame.pack()

        Label(content_frame, text="Welcome to", font=("Helvetica", 26, "bold"), fg="#333", bg="white").pack(pady=(0, 10))
        Label(content_frame, text="Noise Pollution Tracker", font=("Helvetica", 32, "bold  "), fg="#1e90ff", bg="white").pack(pady=(0, 15))
        Label(content_frame, text="Track and manage city noise levels effortlessly.", font=("Arial", 14), fg="#666", bg="white").pack(pady=(0, 30))

        style_btn = Button(content_frame, text="Get Started", font=("Arial", 13, "bold"),
                           bg="#1e90ff", fg="white", activebackground="#0f7ae5", activeforeground="white",
                           relief="flat", padx=25, pady=10, cursor="hand2",
                           command=self.login_page)
        style_btn.pack()

        Label(self.root, text="Designed by Khushwant Saini", font=("Arial", 9), bg="white", fg="#999").place(relx=0.5, rely=0.95, anchor="center")

    def login_page(self):
        self.clear_page()

        left_img_label = Label(self.root, image=self.left_image, bg="white")
        left_img_label.place(x=50, y=70)

        frame = Frame(self.root, width=350, height=350, bg="white")
        frame.place(x=480, y=70)
        heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=100, y=5)
        Label(frame, image=self.icon_user, bg="white").place(x=30, y=80)
        self.user_login_entry = Entry(frame, width=25, fg='black', border=2, bg="white", font=('Microsoft YaHei UI Light', 11))
        self.user_login_entry.place(x=60, y=80)
        self.user_login_entry.insert(0, 'Username')
        self.user_login_entry.bind('<FocusIn>', self.on_enter_user_login)
        self.user_login_entry.bind('<FocusOut>', self.on_leave_user_login)
        Label(frame, image=self.icon_lock, bg="white").place(x=30, y=150)

        self.code_login_entry = Entry(frame, width=25, fg='black', border=2, bg="white", font=('Microsoft YaHei UI Light', 11))
        self.code_login_entry.place(x=60, y=150)
        self.code_login_entry.insert(0, 'Password')
        self.code_login_entry.bind('<FocusIn>', self.on_enter_code_login)
        self.code_login_entry.bind('<FocusOut>', self.on_leave_code_login)

        def password_command():
            if self.code_login_entry.cget('show') == '*':
                self.code_login_entry.config(show='')
            else:
                self.code_login_entry.config(show='*')

        Checkbutton(frame, bg='white', command=password_command, text='Show Password').place(x=60, y=190)
        Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=self.signin).place(x=35, y=230)

        Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9)).place(x=75, y=280)
        Button(frame, width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=self.registration_page).place(x=215, y=280)

    def on_enter_user_login(self, e):
        if self.user_login_entry.get() == 'Username':
            self.user_login_entry.delete(0, 'end')

    def on_leave_user_login(self, e):
        if self.user_login_entry.get() == '':
            self.user_login_entry.insert(0, 'Username')

    def on_enter_code_login(self, e):
        if self.code_login_entry.get() == 'Password':
            self.code_login_entry.delete(0, 'end')
            self.code_login_entry.config(show="*")

    def on_leave_code_login(self, e):
        if self.code_login_entry.get() == '':
            self.code_login_entry.config(show='')
            self.code_login_entry.insert(0, 'Password')

    def registration_page(self):
        self.clear_page()

        left_img_label = Label(self.root, image=self.left_image, bg="white")
        left_img_label.place(x=50, y=70)

        frame = Frame(self.root, width=350, height=350, bg="white")
        frame.place(x=470, y=70)
        Label(frame, text='Sign up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light ', 22)).place(relx=0.5, rely=0.05, anchor=CENTER)
        Label(frame, image=self.icon_email, bg="white").place(x=20, y=95)
        self.name_register_entry = Entry(frame, fg="black", border=1, font=("Microsoft YaHei UI ", 11))
        self.name_register_entry.place(x=50, y=95, width=260, height=25)
        Label(frame, text="Email", fg="black", bg='white', font=("Microsoft YaHei UI ", 11)).place(x=20, y=70)

        Label(frame, image=self.icon_user, bg="white").place(x=20, y=155)
        self.username_register_entry = Entry(frame, fg="black", border=1, font=("Microsoft YaHei UI ", 11))
        self.username_register_entry.place(x=50, y=155, width=260, height=25)
        Label(frame, text='Username', fg="black", bg="white", font=("Microsoft YaHei UI ", 11)).place(x=20, y=130)
        Label(frame, image=self.icon_lock, bg="white").place(x=20, y=215)

        self.password_register_entry = Entry(frame, fg="black", border=1, font=("Microsoft YaHei UI ", 11), show="*")
        self.password_register_entry.place(x=50, y=215, width=260, height=25)
        Label(frame, text='Password', fg="black", bg='white', font=("Microsoft YaHei UI ", 11)).place(x=20, y=190)

        Button(frame, text='Register', bg='#57a1f8', fg='white', border=0, command=self.register_user).place(x=24, y=285, width=286, height=35)

        def toggle_password():
            self.password_register_entry.config(show='' if self.password_register_entry.cget('show') == '*' else '*')

        Checkbutton(frame, bg='white', command=toggle_password, text='Show Password').place(x=24, y=245)
        Button(frame, width=6, text='Back', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=self.login_page).place(x=20, y=20)

    def register_user(self):
        username = self.username_register_entry.get()
        password = self.password_register_entry.get()
        if username and password:
            if username in self.users:
                messagebox.showerror("Registration Failed", "Username already exists.")
            else:
                self.users[username] = password
                messagebox.showinfo("Registration Successful", "Account created successfully ! Please sign in.")
                self.login_page()
        else:
            messagebox.showerror("Registration Failed", "Please enter both username and password.")

    def signin(self):
        username = self.user_login_entry.get()
        password = self.code_login_entry.get()
        if username in self.users and self.users[username] == password:
            messagebox.showinfo("Login Successful", "Welcome to the Noise Pollution Tracker!")
            self.noise_detector_page()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def noise_detector_page(self):
        self.clear_page()

        city_noise_data = {
            'Delhi': 85,
            'Mumbai': 80,
            'Bangalore': 75,
            'Kolkata': 88,
            'Chennai': 82,
            'Hyderabad': 78,
            'Pune': 70,
        }

        def get_noise_level():
            city = city_var.get()
            if city in city_noise_data:
                noise = city_noise_data[city]
                noise_label.config(text=f"Noise Pollution Level in {city}: {noise} dB", image=icon_noise)
                suggestion_label.config(image=icon_warning)

                if noise > 85:
                    suggestion = "High Noise Pollution! Use noise-canceling headphones or earplugs."
                elif 75 < noise <= 85:
                    suggestion = "Moderate Noise. Avoid noisy areas for long periods."
                else:
                    suggestion = "Low Noise Pollution. Enjoy your environment!"

                suggestion_label.config(text=suggestion)

                noise_label.pack(pady=10)
                suggestion_label.pack(pady=5)
            else:
                messagebox.showerror("Error", "City not found!")

        bg_image_path = "C:/Users/DELL/Downloads/noise-backgroundimage.png"
        bg_image = Image.open(bg_image_path).resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        bg_photo = ImageTk.PhotoImage(bg_image)
        canvas = Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")
        self.bg_photo = bg_photo

        icon_noise = PhotoImage(file="C:/Users/DELL/Downloads/noise_icon.png")
        icon_city = PhotoImage(file="C:/Users/DELL/Downloads/city_icon.png")
        icon_warning = PhotoImage(file="C:/Users/DELL/Downloads/warning_icon.png")

        decorative_image = Image.open("C:/Users/DELL/Downloads/decorativeimage.png")
        decorative_image = decorative_image.resize((100, 100))
        decorative_photo = ImageTk.PhotoImage(decorative_image)

        frame = Frame(self.root, bg="white", padx=40, pady=30)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        Label(frame, image=decorative_photo, bg="white").pack(pady=5)
        self.decorative_photo = decorative_photo

        Label(frame, text="Select a city to view noise level", font=("Arial", 14, "bold"), bg="white",
              image=icon_city, compound="left", padx=10).pack(pady=(0, 10))
        self.icon_city = icon_city

        city_var = StringVar(self.root)
        city_var.set("Delhi")
        OptionMenu(frame, city_var, *city_noise_data.keys()).pack(pady=10)

        Button(frame, text="Get Noise Level", command=get_noise_level, bg="black", fg="white").pack(pady=10)

        noise_label = Label(frame, text="", font=("Arial", 12), bg="white", fg="black", compound="left", padx=10)
        suggestion_label = Label(frame, text="", font=("Arial", 10), bg="white", fg="red", compound="left", padx=10)

        self.icon_noise = icon_noise
        self.icon_warning = icon_warning

        Button(frame, width=6, text='Back', border=0, bg='white', cursor='hand2', fg='black', command=self.login_page).pack(pady=(15, 0))

    def clear_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
