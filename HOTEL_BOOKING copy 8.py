import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3
import datetime
import random
import string
from tkinter import messagebox
from PIL import Image, ImageTk


class HotelReservationModel:
    def __init__(self):
        self.pemesan_name = ""
        self.identitas_type = ""
        self.identitas_number = ""
        self.birthdate_dd = ""
        self.birthdate_mm = ""
        self.birthdate_yy = ""
        self.gender = ""
        self.phone_number_right = ""
        self.email_right = ""
        self.checkin_dd = ""
        self.checkin_mm = ""
        self.checkin_yy = ""
        self.checkout_dd = ""
        self.checkout_mm = ""
        self.checkout_yy = ""
        self.room_type = ""
        self.payment_right = ""
        self.order_number = ""
        self.kode_pin = ""

    def create_tables(self):
        with self.conn:
            cursor = self.conn.cursor()
    
    def validate_email(self):
        email = self.email_right.get()
        if '@' not in email and email != "":
            return False
        return True
    
class HotelReservationView:
    def __init__(self, master=None):
        self.root = master or tk.Tk()
        self.root.geometry("1920x1080")
        self.root.title("Luxury Hotels and Resorts | Sandaya Hotels, Resorts")
        self.root.configure(bg="#F0F0FF")
        self.controller = None

        self.create_main_window()
        self.root.mainloop()

    def set_controller(self, controller):
        self.controller = controller

    def create_main_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.frame = Frame(self.root, width=screen_width, height=screen_height)
        self.frame.pack()
        self.frame.place(anchor='center', relx=0.5, rely=0.5)

        img = Image.open("sandya.JPG")
        img = img.resize((screen_width, screen_height), Image.LANCZOS)
        self.img = ImageTk.PhotoImage(img)

        self.label = Label(self.frame, image=self.img)
        self.label.pack()

        i1 = Label(self.root, text="SANDYA", bg="#83838B", fg="white", font=('Dotum', 25))
        i2 = Label(self.root, text="Hotels-Resorts-Spas", fg="white", bg="#83838B", font=('Dotum', 12))
        i1.pack(fill="x")
        i2.pack(fill="x")

        self.frame = Frame(self.root)
        self.frame.pack(side="right", anchor="ne")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        self.frame.configure(bg="") 
        bf = Frame(self.root)
        bf2 = Frame(self.root)
        bf2.pack(side="bottom", anchor="sw")
        bf3 = Frame(self.root)
        bf3.pack(side="bottom", anchor="sw")
        bf.pack(side="bottom")
        bf1 = Frame(self.root)
        bf1.pack(side="bottom", anchor="sw")
        bottomframe = Frame(self.root)
        bottomframe.pack(side="bottom", anchor="se")
        button_frame = Frame(self.root)
        button_frame.place(relx=0.5, rely=0.5, anchor=CENTER)


        i5 = Label(bf, text="© 2024 Sandya Hotels, Resorts & Spas", bg="white", fg="black")
        i5.pack(side="left")
        i6 = Button(bottomframe, text="Privacy Statement", bg="white", fg="black", command=self.open_privacy_page)
        i6.pack(side=RIGHT)
        i7 = Button(bottomframe, text="Cookie Policy", bg="white", fg="black", command=self.open_cookie_page)
        i7.pack(side=RIGHT)
        i8 = Button(bottomframe, text="Terms and Conditions ", bg="white", fg="black", command=self.open_terms_conditions_page)
        i8.pack(side=RIGHT)
        i9 = Label(bf1, text="ANY QUESTIONS?", bg="white", fg="black")
        i9.pack(side="left")
        i12 = Label(bf2, text="Contact Number: +66 2 365 9110", bg="white", fg="black")
        i12.pack(side="left")
        i12 = Label(bf3, text="Email us: reservesandya@sandya.com", bg="white", fg="black") 
        i12.pack(side="left")

        i3 = Button(button_frame, text="CHECK IN", fg='#83838B', command=self.open_signup_page, font=('Dotum', 20, 'bold'), width=20, height=5, highlightthickness=0, bd=0)
        i3.pack(side=LEFT, padx=(0, 0))

        i4 = Button(button_frame, text="CHECK OUT", fg='#83838B', command=self.open_login_page, font=('Dotum', 20, 'bold'), width=20, height=5, highlightthickness=0, bd=0)
        i4.pack(side=RIGHT, padx=(0, 0))

    def open_terms_conditions_page(self):
        self.terms_window = Toplevel(self.root)
        self.terms_window.overrideredirect(True)
        self.terms_window.geometry("600x800")
        self.terms_window.title("Terms and Conditions")
        self.terms_window.configure(bg="#F0F0FF")

        i47 = Label(self.terms_window, text="SANDYA", bg="#83838B", fg="white", font=('Dotum', 25))
        i48 = Label(self.terms_window, text="Hotels-Resorts-Spas", fg="white", bg="#83838B", font=('Dotum', 12))
        i47.pack(fill="x")
        i48.pack(fill="x")

           # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the x and y coordinates to center the window
        x = (screen_width/2) - (600/2)
        y = (screen_height/2) - (800/2)

        # Set the window position
        self.terms_window.geometry(f"+{int(x)}+{int(y)}")

        image = Image.open("terms1.jpg")
        test = ImageTk.PhotoImage(image)
        labell = Label(self.terms_window, image=test)
        labell.image = test
        labell.place(x=0, y=0)

        close_button = Button(self.terms_window, text="Close", command=self.terms_window.destroy, font=('Helvetica', 18), height=2, width=10)
        close_button.pack(side=BOTTOM, pady=50)

    def open_cookie_page(self):
        self.cookie_window = Toplevel(self.root)
        self.cookie_window.overrideredirect(True)
        self.cookie_window.geometry("600x800")
        self.cookie_window.title("Cookie Policy")
        self.cookie_window.configure(bg="#F0F0FF")

        i47 = Label(self.cookie_window, text="SANDYA", bg="#83838B", fg="white", font=('Dotum', 25))
        i48 = Label(self.cookie_window, text="Hotels-Resorts-Spas", fg="white", bg="#83838B", font=('Dotum', 12))
        i47.pack(fill="x")
        i48.pack(fill="x")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the x and y coordinates to center the window
        x = (screen_width/2) - (600/2)
        y = (screen_height/2) - (800/2)

        # Set the window position
        self.cookie_window.geometry(f"+{int(x)}+{int(y)}")

        image = Image.open("cookie.jpg")
        test = ImageTk.PhotoImage(image)
        labell = Label(self.cookie_window, image=test)
        labell.image = test
        labell.place(x=0, y=0)

        close_button = Button(self.cookie_window, text="Close", command=self.cookie_window.destroy, font=('Helvetica', 18), height=2, width=10)
        close_button.pack(side=BOTTOM, pady=50)
    
    def open_privacy_page(self):
        self.privacy_window = Toplevel(self.root)
        self.privacy_window.overrideredirect(True)
        self.privacy_window.geometry("600x800")
        self.privacy_window.title("Cookie Policy")
        self.privacy_window.configure(bg="#F0F0FF")

        i47 = Label(self.privacy_window, text="SANDYA", bg="#83838B", fg="white", font=('Dotum', 25))
        i48 = Label(self.privacy_window, text="Hotels-Resorts-Spas", fg="white", bg="#83838B", font=('Dotum', 12))
        i47.pack(fill="x")
        i48.pack(fill="x")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the x and y coordinates to center the window
        x = (screen_width/2) - (600/2)
        y = (screen_height/2) - (800/2)

        # Set the window position
        self.privacy_window.geometry(f"+{int(x)}+{int(y)}")

        image = Image.open("privacy.jpg")
        test = ImageTk.PhotoImage(image)
        labell = Label(self.privacy_window, image=test)
        labell.image = test
        labell.place(x=0, y=0)

        close_button = Button(self.privacy_window, text="Close", command=self.privacy_window.destroy, font=('Helvetica', 18), height=2, width=10)
        close_button.pack(side=BOTTOM, pady=50)
    
    def open_hotel_log_page(self):
        self.hotel_log_window = Toplevel(self.root)
        self.hotel_log_window.geometry("1600x800")
        self.hotel_log_window.title("Sandya TIPE ROOM")
        self.hotel_log_window.configure(bg="#F0F0FF")

        b = Label(self.hotel_log_window, bg="#F0F0FF", bd=2, relief=RIDGE)
        b.place(relx=0.032, rely=0.1, relheight=0.85, relwidth=0.45)
        a = Label(self.hotel_log_window, bg="#F0F0FF", bd=2, relief=RIDGE)
        a.place(relx=0.52, rely=0.1, relheight=0.85, relwidth=0.45)

        i10 = Label(self.hotel_log_window, text="SANDYA", bg="#83838B", fg="white", font=('Dotum', 25))
        i11 = Label(self.hotel_log_window, text="TIPE ROOM", fg="white", bg="#83838B", font=('Dotum', 12))
        i10.pack(fill="x")
        i11.pack(fill="x")

        i30 = Label(self.hotel_log_window, text="STANDARD ROOM", font=('Dotum', 22, 'bold'))
        i30.place(x=430, y=120)

        image = Image.open("tipestandard.jpg")
        test = ImageTk.PhotoImage(image)
        labell = Label(self.hotel_log_window, image=test)
        labell.image = test
        labell.place(x=70, y=120)

        i31 = Label(self.hotel_log_window, text="*Kamar Ekonomis dengan Sarapan", font=('Dotum', 12, 'bold'), bg="#F0F0FF", fg="#4D4D4D")
        i31.place(x=430, y=170)

        i32 = Label(self.hotel_log_window, text="*Sarapan pagi sudah termasuk", font=('Dotum', 12), bg="#F0F0FF", fg="#4D4D4D")
        i32.place(x=430, y=210)

        i33 = Label(self.hotel_log_window, text="*Harga terjangkau", font=('Dotum', 12, 'bold'), bg="#F0F0FF", fg="#4D4D4D")
        i33.place(x=430, y=250)

        i34 = Label(self.hotel_log_window, text="*Anak-anak menginap tanpa biaya tambahan", font=('Dotum', 12), bg="#F0F0FF", fg="#4D4D4D")
        i34.place(x=430, y=290)

        i35_text = ("Standard Room adalah santapan yang nyaman bagi para pelancong yang mencari kesederhanaan dengan sentuhan kemewahan.\n\n"
            "Setiap kamar dilengkapi dengan desain yang elegan namun hangat, menciptakan suasana yang mengundang untuk bersantai.\n\n"
            "Tempat tidur yang nyaman dengan linen berkualitas tinggi menjanjikan istirahat yang mendalam, sementara fasilitas modern seperti AC,\n"
            "televisi layar datar, dan area kerja memastikan kenyamanan dan produktivitas selama menginap.\n\n"
            "Kamar mandi pribadi yang dilengkapi dengan perlengkapan mandi mewah menambahkan sentuhan kelas atas pada pengalaman menginap Anda.\n\n"
            "Dengan layanan yang ramah dan perhatian terhadap detail, kamar standar di Hotel Sandya adalah tempat yang sempurna untuk menikmati istirahat yang menyegarkan setelah menjelajahi pesona destinasi Anda.")

        i35 = Label(self.hotel_log_window, text=i35_text, font=('Dotum', 11, 'bold'), bg="#F0F0FF", fg="gray", justify="left", wraplength=350,)
        i35.place(x=70, y=380)

        image = Image.open("rate-01.jpg")
        test = ImageTk.PhotoImage(image)
        labell = Label(self.hotel_log_window, image=test)
        labell.image = test
        labell.place(x=430, y=380)

        i30=Label(self.hotel_log_window,text="SUPERIOR ROOM",font=('Dotum',22,'bold'))
        i30.place(x=1145,y=120)
    
        image = Image.open("tipesuperior.jpg")
        test=ImageTk.PhotoImage(image)
        labell=Label(self.hotel_log_window,image=test)
        labell.image=test
        labell.place(x=775,y=120)

        i31 = Label(self.hotel_log_window, text="*Kamar Superior dengan Sarapan", font=('Dotum', 12, 'bold'), bg="#F0F0FF", fg="#4D4D4D")
        i31.place(x=1145, y=170)

        i32 = Label(self.hotel_log_window, text="*Sarapan prasmanan termasuk", font=('Dotum', 12), bg="#F0F0FF", fg="#4D4D4D")
        i32.place(x=1145, y=210)

        i33 = Label(self.hotel_log_window, text="*Pemandangan indah", font=('Dotum', 12, 'bold'), bg="#F0F0FF", fg="#4D4D4D")
        i33.place(x=1145, y=250)

        i34 = Label(self.hotel_log_window, text="*Akses langsung ke kolam renang", font=('Dotum', 12), bg="#F0F0FF", fg="#4D4D4D")
        i34.place(x=1145, y=290)

        i35_text = ("Superior Room di Hotel Sandya adalah pilihan yang nyaman dan elegan untuk para tamu yang menginginkan kenyamanan dan kelas di tengah kunjungan mereka.\n\n "
            "Kamar ini biasanya dilengkapi dengan fasilitas modern seperti tempat tidur yang luas, area duduk santai, TV layar datar, akses Wi-Fi gratis, brankas untuk menyimpan barang berharga,\n\n"
            "serta fasilitas pembuat kopi dan teh untuk menikmati minuman hangat di waktu luang, serta kamar mandi pribadi yang dilengkapi dengan perlengkapan mandi yang lengkap.\n\n"
            "Dengan sentuhan desain yang elegan dan perabotan yang berkualitas, Anda dapat menikmati pengalaman menginap yang menyenangkan dan memuaskan selama kunjungan Anda di Hotel Sandya.")

        i35 = Label(self.hotel_log_window, text=i35_text, font=('Dotum', 11, 'bold'), bg="#F0F0FF", fg="gray", justify="left", wraplength=350)
        i35.place(x=775, y=380)

        image = Image.open("rate-02.jpg")
        test=ImageTk.PhotoImage(image)
        labell=Label(self.hotel_log_window,image=test)
        labell.image=test
        labell.place(x=1145,y=380)

        ce30 = Button(self.hotel_log_window, text="BOOK NOW", command=lambda: self.open_booking_page(self.hotel_log_window), font=('Dotum', 14, 'bold'))
        ce30.place(x=488, y=520)

        ce30 = Button(self.hotel_log_window, text="BOOK NOW", command=lambda: self.open_booking_page(self.hotel_log_window), font=('Dotum', 14, 'bold'))
        ce30.place(x=1220, y=520)

        ce62 = Button(self.hotel_log_window, text="<<", command=self.ask_leave_hotel_page, font=('Dotum', 10))
        ce62.pack(side="left")
        
        ce600 = Button(self.hotel_log_window, text=">>", command=lambda: self.open_hotel_log_page_A(self.hotel_log_window),font=('Dotum', 10))
        ce600.pack(side="right")

    def ask_leave_hotel_page(self):
        if messagebox.askokcancel("Peringatan", "Apakah Anda Yakin Ingin Meninggalkan Halaman Ini?"):
           self.hotel_log_window.destroy() 

    def open_hotel_log_page_A(self, previous_window):
        self.hotel_log_A_window = Toplevel(self.root)
        self.hotel_log_A_window.geometry("1600x800")
        self.hotel_log_A_window.title("Sandya TIPE ROOM")
        self.hotel_log_A_window.configure(bg="#F0F0FF")

        b = Label(self.hotel_log_A_window, bg="#F0F0FF", bd=2, relief=RIDGE)
        b.place(relx=0.032, rely=0.1, relheight=0.85, relwidth=0.45)
        a = Label(self.hotel_log_A_window, bg="#F0F0FF", bd=2, relief=RIDGE)
        a.place(relx=0.52, rely=0.1, relheight=0.85, relwidth=0.45)

        i101 = Label(self.hotel_log_A_window, text="SANDYA", bg="#83838B", fg="white", font=('Dotum', 25))
        i111 = Label(self.hotel_log_A_window, text="TIPE ROOM", fg="white", bg="#83838B", font=('Dotum', 12))
        i101.pack(fill="x")
        i111.pack(fill="x")

        i301 = Label(self.hotel_log_A_window, text="SUITE ROOM", font=('Dotum', 22, 'bold'))
        i301.place(x=430, y=120)

        image = Image.open("tipesuite.jpg")
        test = ImageTk.PhotoImage(image)
        labell1 = Label(self.hotel_log_A_window, image=test)
        labell1.image = test
        labell1.place(x=70, y=120)

        i311 = Label(self.hotel_log_A_window, text="*Kamar Suite dengan Sarapan", font=('Dotum', 12, 'bold'), bg="#F0F0FF", fg="#4D4D4D")
        i311.place(x=430, y=170)

        i321=Label(self.hotel_log_A_window,text="*Sarapan eksklusif termasuk", font=('Dotum', 12,), bg="#F0F0FF", fg="#4D4D4D")
        i321.place(x=430,y=210)

        i331=Label(self.hotel_log_A_window,text="*Ruang tamu terpisah", font=('Dotum', 12, 'bold'), bg="#F0F0FF", fg="#4D4D4D")
        i331.place(x=430,y=250)

        i341=Label(self.hotel_log_A_window,text="*Akses gratis ke spa dan kolam renang",  font=('Dotum', 12,), bg="#F0F0FF", fg="#4D4D4D")
        i341.place(x=430,y=290)

        i351_text = ("Suite Room di Hotel Sandya adalah pilihan yang menghadirkan kemewahan dan kenyamanan tingkat atas bagi para tamu yang mencari pengalaman istimewa selama menginap.\n\n "
                    "Setiap Suite Room dirancang dengan desain yang elegan dan menawarkan ruang yang luas untuk bersantai dan menikmati waktu bersama.\n\n"
                    "Fasilitasnya mencakup tempat tidur yang nyaman dengan linen berkualitas, area duduk yang luas, TV layar datar, akses Wi-Fi gratis, brankas untuk menyimpan barang berharga, fasilitas pembuat kopi dan teh, serta kamar mandi pribadi yang dilengkapi dengan perlengkapan mandi mewah.\n\n"
                    "Dengan sentuhan desain yang mengagumkan dan perabotan yang berkualitas, Suite Room di Hotel Sandya menjanjikan pengalaman menginap yang istimewa dan memuaskan bagi para tamu yang menginginkan tingkat kelas dan kenyamanan yang tinggi.")

        i351 = Label(self.hotel_log_A_window, text=i351_text, font=('Dotum', 11, 'bold'), bg="#F0F0FF", fg="gray", justify="left", wraplength=350)
        i351.place(x=70, y=380)
            

        image = Image.open("rate-03.jpg")
        test = ImageTk.PhotoImage(image)
        labell1 = Label(self.hotel_log_A_window, image=test)
        labell1.image = test
        labell1.place(x=430, y=380)

        i301=Label(self.hotel_log_A_window,text="PRESIDENTIAL ROOM",font=('Dotum',22,'bold'))
        i301.place(x=1145,y=120)
    
        image = Image.open("tipepresidential.jpg")
        test=ImageTk.PhotoImage(image)
        labell1=Label(self.hotel_log_A_window,image=test)
        labell1.image=test
        labell1.place(x=775,y=120)

        i311=Label(self.hotel_log_A_window,text="*Kamar Presidential dengan Sarapan", font=('Dotum', 12, 'bold'), bg="#F0F0FF", fg="#4D4D4D")   
        i311.place(x=1145,y=170)

        i321=Label(self.hotel_log_A_window,text="*Sarapan mewah termasuk",font=('Dotum', 12,), bg="#F0F0FF", fg="#4D4D4D")
        i321.place(x=1145,y=210)

        i331=Label(self.hotel_log_A_window,text="*Fasilitas VIP", font=('Dotum', 12, 'bold'), bg="#F0F0FF", fg="#4D4D4D")
        i331.place(x=1145,y=250)
    
        i341=Label(self.hotel_log_A_window,text="*Layanan butler pribadi", font=('Dotum', 12,), bg="#F0F0FF", fg="#4D4D4D")
        i341.place(x=1145,y=290)

        i351_text = ("Presidential Room di Hotel Sandya adalah simbol kemewahan dan eksklusivitas yang memukau para tamu dengan pengalaman menginap yang tak terlupakan.\n\n "
        "Setiap Presidential Room dirancang dengan detail yang sempurna, menawarkan ruang yang luas dan fasilitas yang luar biasa.\n\n"
        "Kamar ini dilengkapi dengan tempat tidur mewah yang sangat nyaman, ruang tamu yang elegan, ruang makan pribadi, area kerja eksklusif, dan balkon pribadi yang menawarkan pemandangan indah.\n\n"
        "Fasilitas modern seperti TV layar datar, akses Wi-Fi gratis, brankas untuk menyimpan barang berharga, minibar, dan kamar mandi mewah dengan bathtub jacuzzi dan perlengkapan mandi berkualitas tinggi juga tersedia untuk memenuhi kebutuhan dan kenyamanan tamu.\n\n"
        "Dengan pelayanan yang sangat baik dan perhatian terhadap detail, Presidential Room di Hotel Sandya menawarkan pengalaman menginap yang istimewa bagi tamu yang menghargai kemewahan dan privasi.")

        i351 = Label(self.hotel_log_A_window, text=i351_text, font=('Dotum', 11, 'bold'), bg="#F0F0FF", fg="gray", justify="left", wraplength=350)
        i351.place(x=775, y=380)
        

        image = Image.open("rate-04.jpg")
        test=ImageTk.PhotoImage(image)
        label1l=Label(self.hotel_log_A_window,image=test)
        label1l.image=test
        label1l.place(x=1145,y=380)

        ce30 = Button(self.hotel_log_A_window, text="BOOK NOW", command=lambda: self.open_booking_page(self.hotel_log_A_window), font=('Dotum', 14, 'bold'))
        ce30.place(x=488, y=520)

        ce30 = Button(self.hotel_log_A_window, text="BOOK NOW", command=lambda: self.open_booking_page(self.hotel_log_A_window), font=('Dotum', 14, 'bold'))
        ce30.place(x=1220, y=520)

        ce600 = Button(self.hotel_log_A_window, text="<<", command=lambda: previous_window.lift(), font=('Dotum', 10))
        ce600.pack(side="left")

        ce60 = Button(self.hotel_log_A_window, text=">>", command=lambda: self.open_hotel_fasilitas_page(self.hotel_log_A_window),font=('Dotum', 10))
        ce60.pack(side="right")
    
    def open_hotel_fasilitas_page(self, previous_window):
        self.hotel_fasilitas_window = Toplevel(self.root)
        self.hotel_fasilitas_window.geometry("1600x800")
        self.hotel_fasilitas_window.title("Sandya TIPE ROOM")
        self.hotel_fasilitas_window.configure(bg="#F0F0FF")

        b = Label(self.hotel_fasilitas_window, bg="#F0F0FF", bd=2, relief=RIDGE)
        b.place(relx=0.032, rely=0.1, relheight=0.85, relwidth=0.45)
        a = Label(self.hotel_fasilitas_window, bg="#F0F0FF", bd=2, relief=RIDGE)
        a.place(relx=0.52, rely=0.1, relheight=0.85, relwidth=0.45)

        i100 = Label(self.hotel_fasilitas_window, text="SANDYA", bg="#83838B", fg="white", font=('Dotum', 25))
        i110 = Label(self.hotel_fasilitas_window, text="FASILITAS HOTELS", fg="white", bg="#83838B", font=('Dotum', 12))
        i100.pack(fill="x")
        i110.pack(fill="x")

        i300 = Label(self.hotel_fasilitas_window, text="RESTORANT", font=('Dotum', 22, 'bold'))
        i300.place(x=430, y=120)

        image = Image.open("resto.jpg")
        test = ImageTk.PhotoImage(image)
        labell = Label(self.hotel_fasilitas_window, image=test)
        labell.image = test
        labell.place(x=70, y=120)

        i310 = Label(self.hotel_fasilitas_window, text="*Buka untuk Sarapan dan Makan Malam", font=('Dotum', 12, 'bold'), bg="#F0F0FF", fg="#4D4D4D")
        i310.place(x=430, y=170)

        i320 = Label(self.hotel_fasilitas_window, text="*Beragam masakan lokal dan internasional", font=('Dotum', 12), bg="#F0F0FF", fg="#4D4D4D")
        i320.place(x=430, y=210)

        i330 = Label(self.hotel_fasilitas_window, text="*Koki berpengalaman dan terkenal", font=('Dotum', 12, 'bold'), bg="#F0F0FF", fg="#4D4D4D")
        i330.place(x=430, y=250)

        i340 = Label(self.hotel_fasilitas_window, text="*Suasana makan yang nyaman dan elegan", font=('Dotum', 12), bg="#F0F0FF", fg="#4D4D4D")
        i340.place(x=430, y=290)
        
        i350_text = ("Hotel Sandya adalah sebuah hotel yang terletak di kawasan strategis dan menawarkan berbagai fasilitas unggulan bagi para tamu.\n\n\n"
              "Salah satu fasilitas yang paling menonjol adalah restorannya. Restoran di Hotel Sandya terkenal dengan suasana yang nyaman dan menu yang beragam,\n\n"
              "yang mencakup hidangan lokal dan internasional. Chef berpengalaman di restoran ini menggunakan bahan-bahan segar dan berkualitas\n\n"
              "untuk menciptakan hidangan yang memuaskan selera para tamu. Selain itu, restoran ini juga menawarkan layanan room service bagi tamu\n\n"
              "yang ingin menikmati hidangan di kenyamanan kamar mereka. Dengan pelayanan yang ramah dan profesional, restoran di Hotel Sandya\n\n"
              "menjadi pilihan tepat bagi tamu yang mencari pengalaman kuliner yang istimewa selama menginap.")

        i350 = Label(self.hotel_fasilitas_window, text=i350_text, font=('Dotum', 11, 'bold'), bg="#F0F0FF", fg="gray", justify="left", wraplength=350,)
        i350.place(x=70, y=380)

        i300=Label(self.hotel_fasilitas_window,text="KOLAM RENANG",font=('Dotum',22,'bold'))
        i300.place(x=1130,y=120)
    
        image = Image.open("kolamrenang.jpg")
        test=ImageTk.PhotoImage(image)
        labell=Label(self.hotel_fasilitas_window,image=test)
        labell.image=test
        labell.place(x=775,y=120)

        i310 = Label(self.hotel_fasilitas_window, text="*Kolam renang tersedia untuk tamu", font=('Dotum', 12, 'bold'), bg="#F0F0FF", fg="#4D4D4D")
        i310.place(x=1130, y=170)

        i320 = Label(self.hotel_fasilitas_window, text="*Kolam renang dalam dan luar ruangan", font=('Dotum', 12), bg="#F0F0FF", fg="#4D4D4D")
        i320.place(x=1130, y=210)

        i330= Label(self.hotel_fasilitas_window, text="*Fasilitas kolam renang anak-anak", font=('Dotum', 12, 'bold'), bg="#F0F0FF", fg="#4D4D4D")
        i330.place(x=1130, y=250)

        i340= Label(self.hotel_fasilitas_window, text="*Tersedia layanan penyewaan handuk", font=('Dotum', 12), bg="#F0F0FF", fg="#4D4D4D")
        i340.place(x=1130, y=290)
        
        i350_text = ("Kolam renang Hotel Sandya adalah fasilitas unggulan yang dirancang untuk memberikan pengalaman relaksasi terbaik bagi para tamu.\n\n"
             "Terletak di lingkungan yang asri, kolam renang ini menawarkan pemandangan indah dan suasana yang tenang, cocok untuk bersantai dan melepas penat.\n\n"
             "Kolam renang dilengkapi dengan area berjemur yang nyaman serta layanan poolside bar yang menyediakan berbagai macam minuman dan makanan ringan.\n\n"
             "Selain itu, kolam renang ini dirancang dengan mempertimbangkan keselamatan, dilengkapi dengan penjaga kolam renang yang terlatih dan berbagai fasilitas pendukung seperti shower dan ruang ganti.\n\n"
             "Baik untuk berenang santai maupun berolahraga, kolam renang Hotel Sandya adalah tempat yang ideal untuk menikmati waktu luang Anda.")

        i350 = Label(self.hotel_fasilitas_window, text=i350_text, font=('Dotum', 11, 'bold'), bg="#F0F0FF", fg="gray", justify="left", wraplength=350)
        i350.place(x=775, y=380)


        ce620 = Button(self.hotel_fasilitas_window, text="<<", command=lambda: previous_window.lift(), font=('Dotum', 10))
        ce620.pack(side="left")
        
        ce600 = Button(self.hotel_fasilitas_window, text=">>", command=lambda: self.open_hotel_fasilitas_page_A(self.hotel_fasilitas_window),font=('Dotum', 10))
        ce600.pack(side="right")


    def open_hotel_fasilitas_page_A(self, previous_window):
        self.hotel_fasilitas_A_window = Toplevel(self.root)
        self.hotel_fasilitas_A_window.geometry("1600x800")
        self.hotel_fasilitas_A_window.title("Sandya FASILITAS HOTELS")
        self.hotel_fasilitas_A_window.configure(bg="#F0F0FF")

        b = Label(self.hotel_fasilitas_A_window, bg="#F0F0FF", bd=2, relief=RIDGE)
        b.place(relx=0.032, rely=0.1, relheight=0.85, relwidth=0.45)
        a = Label(self.hotel_fasilitas_A_window, bg="#F0F0FF", bd=2, relief=RIDGE)
        a.place(relx=0.52, rely=0.1, relheight=0.85, relwidth=0.45)

        i1011 = Label(self.hotel_fasilitas_A_window, text="SANDYA", bg="#83838B", fg="white", font=('Dotum', 25))
        i1111 = Label(self.hotel_fasilitas_A_window, text="FASILITAS HOTELS", fg="white", bg="#83838B", font=('Dotum', 12))
        i1011.pack(fill="x")
        i1111.pack(fill="x")

        i3011 = Label(self.hotel_fasilitas_A_window, text="GYM FITNESS", font=('Dotum', 22, 'bold'))
        i3011.place(x=430, y=120)

        image = Image.open("gym.jpg")
        test = ImageTk.PhotoImage(image)
        labell1 = Label(self.hotel_fasilitas_A_window, image=test)
        labell1.image = test
        labell1.place(x=70, y=120)

        i3111 = Label(self.hotel_fasilitas_A_window, text="*Pusat kebugaran tersedia untuk tamu", font=('Dotum', 12, 'bold'), bg="#F0F0FF", fg="#4D4D4D")
        i3111.place(x=430, y=170)

        i3211=Label(self.hotel_fasilitas_A_window,text="*Peralatan gym lengkap dan modern", font=('Dotum', 12,), bg="#F0F0FF", fg="#4D4D4D")
        i3211.place(x=430,y=210)

        i3311=Label(self.hotel_fasilitas_A_window,text="*Instruktur kebugaran berpengalaman", font=('Dotum', 12, 'bold'), bg="#F0F0FF", fg="#4D4D4D")
        i3311.place(x=430,y=250)

        i3411=Label(self.hotel_fasilitas_A_window,text="*Kelas kebugaran harian tersedia", font=('Dotum', 12,), bg="#F0F0FF", fg="#4D4D4D")
        i3411.place(x=430,y=290)
        
        i3511_text = ("Kolam Gym Fitness Hotel Sandya adalah fasilitas kebugaran yang tersedia di Hotel Sandya.\n\n"
            "Fasilitas ini dilengkapi dengan berbagai peralatan modern untuk latihan kardio dan kekuatan, termasuk treadmill, sepeda statis, dan alat angkat beban.\n\n"
            "Kolam renang di hotel ini menawarkan tempat yang ideal untuk berenang santai atau berolahraga air.\n\n"
            "Area gym dan kolam ini dirancang untuk memenuhi kebutuhan tamu yang ingin menjaga kebugaran selama menginap, dengan suasana yang nyaman dan pelayanan profesional.\n\n"
            "Hotel Sandya memastikan kebersihan dan kenyamanan area gym dan kolam renang untuk memberikan pengalaman yang menyenangkan bagi para tamu.")

        i3511 = Label(self.hotel_fasilitas_A_window, text=i3511_text, font=('Dotum', 11, 'bold'), bg="#F0F0FF", fg="gray", justify="left", wraplength=350)
        i3511.place(x=70, y=380)

        i3011=Label(self.hotel_fasilitas_A_window,text="SPA",font=('Dotum',22,'bold'))
        i3011.place(x=1130,y=120)
    
        image = Image.open("spa.jpg")
        test=ImageTk.PhotoImage(image)
        labell1=Label(self.hotel_fasilitas_A_window,image=test)
        labell1.image=test
        labell1.place(x=775,y=120)

        i3111=Label(self.hotel_fasilitas_A_window,text="*Spa tersedia untuk tamu", font=('Dotum', 12, 'bold'), bg="#F0F0FF", fg="#4D4D4D")   
        i3111.place(x=1130,y=170)

        i3211=Label(self.hotel_fasilitas_A_window,text="*Beragam perawatan dan pijat", font=('Dotum', 12,), bg="#F0F0FF", fg="#4D4D4D")
        i3211.place(x=1130,y=210)

        i3311=Label(self.hotel_fasilitas_A_window, text="*Terapis profesional dan berpengalaman", font=('Dotum', 12, 'bold'), bg="#F0F0FF", fg="#4D4D4D")
        i3311.place(x=1130,y=250)
    
        i3411=Label(self.hotel_fasilitas_A_window, text="*Suasana relaksasi yang tenang dan nyaman", font=('Dotum', 12,), bg="#F0F0FF", fg="#4D4D4D")
        i3411.place(x=1130,y=290)

        i3511_text = ("Spa di Hotel Sandya adalah tempat yang dirancang untuk memberikan pengalaman relaksasi dan kebugaran yang mewah bagi para tamu.\n\n"
            "Terletak di lingkungan yang tenang dan penuh dengan kemewahan, spa ini menawarkan berbagai layanan seperti pijat tradisional, perawatan kulit, dan perawatan tubuh yang menenangkan.\n\n"
            "Staf terlatih dengan baik siap memberikan pelayanan terbaik dengan menggunakan produk-produk berkualitas tinggi untuk memastikan kenyamanan dan kepuasan tamu.\n\n"
            "Suasana yang tenang dan fasilitas modern spa di Hotel Sandya menciptakan pengalaman yang mendalam dalam merawat tubuh dan pikiran, sehingga tamu dapat pulih sepenuhnya dan merasa segar kembali setelah menghabiskan waktu di sini.")

        i3511 = Label(self.hotel_fasilitas_A_window, text=i3511_text, font=('Dotum', 11, 'bold'), bg="#F0F0FF", fg="gray", justify="left", wraplength=350)
        i3511.place(x=775, y=380)

        ce6001 = Button(self.hotel_fasilitas_A_window, text="<<", command=lambda: previous_window.lift(), font=('Dotum', 10))
        ce6001.pack(side="left")



    def open_booking_page(self, previous_window):
        self.booking_window = Toplevel(self.root)
        self.booking_window.geometry("1920x1080")
        self.booking_window.title("BOOKING PAGE")
        self.booking_window.configure(bg="#F0F0FF")

        
        image = Image.open("bookingpagee1.jpg")
        test = ImageTk.PhotoImage(image)
        labell = Label(self.booking_window, image=test)
        labell.image = test
        labell.place(x=0, y=0)

        # Create a frame for the title and label
        title_frame = Frame(self.booking_window)
        title_frame.pack(pady=83)

        
        # Header
        i51 = Label(self.booking_window, text="SANDYA", bg="#83838B", fg="white", font=('Dotum', 25))
        i52 = Label(self.booking_window, text="Booking Page", fg="white", bg="#83838B", font=('Dotum', 12))
        i51.pack(fill="x")
        i52.pack(fill="x")
       
        b = Label(self.booking_window, bg="#F0F0FF", bd=10, relief=RIDGE, highlightbackground="white", highlightthickness=2)
        b.place(relx=0.032, rely=0.3, relheight=0.492, relwidth=0.45)

        a = Label(self.booking_window, bg="#F0F0FF", bd=10, relief=RIDGE, highlightbackground="white", highlightthickness=2)
        a.place(relx=0.52, rely=0.3, relheight=0.492, relwidth=0.45)
        

        # Left Frame (Booking Details)
        left_frame = Frame(self.booking_window, bg="#F0F0FF")
        left_frame.pack(side="left", fill="y")

      
# Formulir
        self.pemesan_name = StringVar()
        self.identitas_type = StringVar()
        self.identitas_number = StringVar()
        self.birthdate = StringVar()
        self.gender = StringVar()
        self.address = StringVar()
        self.phone_number_right = StringVar()
        self.email_right = StringVar()
        self.checkin_right = StringVar()
        self.checkout_right = StringVar()
        self.room_type = StringVar()
        self.payment_right = StringVar()

        b = Label(self.booking_window, bd=2, relief=RIDGE)
        b.place(relx=0.032, rely=0.3, relheight=0.485, relwidth=0.45)

        label_frame = Frame(b)
        label_frame.pack(pady=8, fill="x")

        Label(label_frame, text="Nama Pemesan", font=('Dotum', 14,'bold')).grid(row=0, column=0, padx=50, pady=10, sticky='w')
        self.entry_pemesan_name = Entry(label_frame, bd=5, textvar=self.pemesan_name, width=30, font=('Dotum', 14))
        self.entry_pemesan_name.grid(row=0, column=1, padx=10, pady=10)

        Label(label_frame, text="Kartu Identitas", font=('Dotum', 14,'bold')).grid(row=1, column=0, padx=50, pady=10, sticky='w')

        self.identitas_type = StringVar()
        self.identitas_type.set("KTP")  # default value

        frame_identitas = Frame(label_frame)
        frame_identitas.grid(row=1, column=1, padx=50, pady=8)

        Radiobutton(frame_identitas, text="KTP", variable=self.identitas_type, value="KTP").pack(side=LEFT,)
        Radiobutton(frame_identitas, text="KK", variable=self.identitas_type, value="KK").pack(side=LEFT)
        Radiobutton(frame_identitas, text="PASPOR", variable=self.identitas_type, value="PASPOR").pack(side=LEFT)

        Label(label_frame, text="No. Identitas", font=('Dotum', 14,'bold')).grid(row=2, column=0, padx=50, pady=10, sticky='w')

        def invalid_input(P):
            if not P.isdigit() and P != "":
                messagebox.showerror("Error", "Harap masukkan Hanya Angka Pada Kolom Nomor Identitas.")
            elif len(P) > 16 and P != "":
                messagebox.showerror("Error", "Nomor Identitas Harus 16 digit.")

        vcmd = (label_frame.register(lambda P: P.isdigit() and len(P) <= 16 or P == ""), '%P')
        icmd = (label_frame.register(invalid_input), '%P')

        self.entry_identitas_number = Entry(label_frame, bd=5, textvariable=self.identitas_number, width=30, font=('Dotum', 14), validate='key', validatecommand=vcmd, invalidcommand=icmd)
        self.entry_identitas_number.grid(row=2, column=1, padx=50, pady=10)

        Label(label_frame, text="Tanggal Lahir", font=('Dotum', 14,'bold')).grid(row=3, column=0, padx=50, pady=10, sticky='w')

        inner_frame = Frame(label_frame)
        inner_frame.grid(row=3, column=1, padx=(0, 5), pady=8, sticky='w')
        self.birthdate_dd = ttk.Combobox(inner_frame, state="readonly", width=5, font=('Dotum', 12))
        self.birthdate_dd['values'] = [f"{i:02}" for i in range(1, 32)]
        self.birthdate_dd.current(datetime.date.today().day - 1)  # Set default to current day
        self.birthdate_dd.grid(row=0, column=0, padx=50, pady=8, sticky='w')

        self.birthdate_mm = ttk.Combobox(inner_frame, state="readonly", width=5, font=('Dotum', 12))
        self.birthdate_mm['values'] = [f"{i:02}" for i in range(1, 13)]
        self.birthdate_mm.current(datetime.date.today().month - 1)  # Set default to current month
        self.birthdate_mm.grid(row=0, column=1, padx=5, pady=8, sticky='w')

        self.birthdate_yy = ttk.Combobox(inner_frame, state="readonly", width=8, font=('Dotum', 12))
        self.birthdate_yy['values'] = [str(i) for i in range(datetime.date.today().year - 100, datetime.date.today().year + 1)]
        self.birthdate_yy.current(100)  # Set default to current year (assuming the list is in ascending order)
        self.birthdate_yy.grid(row=0, column=2, padx=5, pady=8, sticky='w')


        Label(label_frame, text="Jenis Kelamin", font=('Dotum', 14,'bold')).grid(row=4, column=0, padx=50, pady=10, sticky='w')

        self.gender = StringVar()
        self.gender.set("0")  

        frame_gender = Frame(label_frame)
        frame_gender.grid(row=4, column=1, padx=50, pady=10)

        Radiobutton(frame_gender, text="Laki-laki", variable=self.gender, value="Laki-laki").pack(side=LEFT)
        Radiobutton(frame_gender, text="Perempuan", variable=self.gender, value="Perempuan").pack(side=LEFT)

        Label(label_frame, text="Alamat*", font=('Dotum', 14,'bold')).grid(row=5, column=0, padx=50, pady=10, sticky='w')
        self.text_address = Text(label_frame, width=30, height=5, font=('Dotum', 14))
        self.text_address.grid(row=5, column=1, padx=50, pady=5)


       # frame right
        a = Label(self.booking_window, bd=2, relief=RIDGE)
        a.place(relx=0.52, rely=0.3, relheight=0.485, relwidth=0.45)

        label_frame_right = Frame(a)
        label_frame_right.pack(pady=8, fill="x")

        # Form elements on the right side
        Label(label_frame_right, text="No. Telp", font=('Dotum', 14,'bold')).grid(row=0, column=0, padx=50, pady=10, sticky='w')

        def invalid_input_phone(P):
            if not P.isdigit() and P != "":
                messagebox.showerror("Error", "Harap Masukkan Hanya Angka Pada Kolom Nomor Telepon.")
            elif len(P) > 13:
                messagebox.showerror("Error", "Nomor Telepon harus terdiri dari maksimal 13 digit.")
            elif len(P) < 13 and P != "":
                messagebox.showerror("Error", "Nomor Telepon harus 13 digit.")

        vcmd_phone = (label_frame_right.register(lambda P: P.isdigit() and len(P) <= 13 or P == ""), '%P')
        icmd_phone = (label_frame_right.register(invalid_input_phone), '%P')

        self.entry_phone_number_right = Entry(label_frame_right, bd=5, textvariable=self.phone_number_right, width=30, font=('Dotum', 14), validate='key', validatecommand=vcmd_phone, invalidcommand=icmd_phone)
        self.entry_phone_number_right.grid(row=0, column=1, padx=50, pady=10)

        Label(label_frame_right, text="Email*", font=('Dotum', 14,'bold')).grid(row=1, column=0, padx=50, pady=10, sticky='w')

        self.entry_email_right = Entry(label_frame_right, bd=5, textvariable=self.email_right, width=30, font=('Dotum', 14))
        self.entry_email_right.grid(row=1, column=1, padx=50, pady=10)

        self.entry_email_right.bind('<KeyRelease>', self.validate_email)

        Label(label_frame_right, text="Tanggal Check in", font=('Dotum', 14,'bold')).grid(row=2, column=0, padx=50, pady=10, sticky='w')

        inner_frame = Frame(label_frame_right)
        inner_frame.grid(row=2, column=1, padx=(0, 5), pady=8, sticky='w')

        self.checkin_dd = ttk.Combobox(inner_frame, state="disable", width=5, font=('Dotum', 12))
        self.checkin_dd['values'] = [f"{i:02}" for i in range(1, 32)]
        self.checkin_dd.set(datetime.date.today().day)  # set default value to today's day
        self.checkin_dd.grid(row=0, column=0, padx=50, pady=8, sticky='w')

        self.checkin_mm = ttk.Combobox(inner_frame, state="disable", width=5, font=('Dotum', 12))
        self.checkin_mm['values'] = [f"{i:02}" for i in range(1, 13)]
        self.checkin_mm.set(datetime.date.today().month)  # set default value to today's month
        self.checkin_mm.grid(row=0, column=1, padx=5, pady=8, sticky='w')

        self.checkin_yy = ttk.Combobox(inner_frame, state="disable", width=8, font=('Dotum', 12))
        self.checkin_yy['values'] = [str(i) for i in range(datetime.date.today().year, datetime.date.today().year + 4)]
        self.checkin_yy.set(datetime.date.today().year)  # set default value to today's year
        self.checkin_yy.grid(row=0, column=2, padx=5, pady=8, sticky='w')

        Label(label_frame_right, text="Tanggal Check out", font=('Dotum', 14,'bold')).grid(row=3, column=0, padx=(50, 10), pady=10, sticky='w')

        inner_frame_checkout = Frame(label_frame_right)
        inner_frame_checkout.grid(row=3, column=1, padx=(0, 5), pady=8, sticky='w')

        self.checkout_dd = ttk.Combobox(inner_frame_checkout, state="readonly", width=5, font=('Dotum', 12))
        self.checkout_dd['values'] = [f"{i:02}" for i in range(1, 32)]
        self.checkout_dd.current(datetime.date.today().day - 1)  # Set default to current day
        self.checkout_dd.grid(row=0, column=0, padx=50, pady=8, sticky='w')

        self.checkout_mm = ttk.Combobox(inner_frame_checkout, state="readonly", width=5, font=('Dotum', 12))
        self.checkout_mm['values'] = [f"{i:02}" for i in range(1, 13)]
        self.checkout_mm.current(datetime.date.today().month - 1)  # Set default to current month
        self.checkout_mm.grid(row=0, column=1, padx=5, pady=8, sticky='w')

        self.checkout_yy = ttk.Combobox(inner_frame_checkout, state="readonly", width=8, font=('Dotum', 12))
        self.checkout_yy['values'] = [str(i) for i in range(datetime.date.today().year, datetime.date.today().year + 1)]
        self.checkout_yy.current(0)  # Set default to current year (assuming the list is in ascending order)
        self.checkout_yy.grid(row=0, column=2, padx=5, pady=8, sticky='w')

        self.checkout_right = StringVar()
  

        def validate_checkout_date():
            checkout_date = datetime.date(int(self.checkout_yy.get()), int(self.checkout_mm.get()), int(self.checkout_dd.get()))
            today = datetime.date.today()
            if checkout_date < today:
                messagebox.showerror("Error", "Tanggal Check out tidak boleh kurang dari hari ini.")
                self.checkout_dd.set(f"{today.day:02}")
                self.checkout_mm.set(f"{today.month:02}")
                self.checkout_yy.set(str(today.year))
        self.checkout_dd.bind("<<ComboboxSelected>>", lambda event: (self.checkout_right.set(f"{self.checkout_dd.get()} / {self.checkout_mm.get()} / {self.checkout_yy.get()}"), validate_checkout_date()))
        self.checkout_mm.bind("<<ComboboxSelected>>", lambda event: (self.checkout_right.set(f"{self.checkout_dd.get()} / {self.checkout_mm.get()} / {self.checkout_yy.get()}"), validate_checkout_date()))
        self.checkout_yy.bind("<<ComboboxSelected>>", lambda event: (self.checkout_right.set(f"{self.checkout_dd.get()} / {self.checkout_mm.get()} / {self.checkout_yy.get()}"), validate_checkout_date()))

        Label(label_frame_right, text="Tipe Kamar", font=('Dotum', 14,'bold')).grid(row=4, column=0, padx=50, pady=10, sticky='w')

        frame_room_type = Frame(label_frame_right)
        frame_room_type.grid(row=4, column=1, padx=60, pady=15)

        options = ["Standard ( Rp139.060,00 )", "Superior ( Rp165.368,00 )", "Suite ( Rp171.982,00 )", "Presidential ( Rp648.241,00 )"]
        self.room_type = StringVar()

        combo_box = ttk.Combobox(frame_room_type, textvariable=self.room_type)
        combo_box['values'] = options
        combo_box.config(state='readonly')  # disable typing
        combo_box.pack(side=LEFT, padx= 9)

        Label(label_frame_right, text="Metode Pembayaran", font=('Dotum', 14,'bold')).grid(row=5, column=0, padx=50, pady=10, sticky='w')

        self.payment_right = StringVar()
        self.payment_right.set("0")  # default value

        frame_payment = Frame(label_frame_right)
        frame_payment.grid(row=5, column=1, padx=60, pady=15)

        options = ["QRIS", "GOPAY", "OVO", "DANA"]
        for option in options:
            rb = ttk.Radiobutton(frame_payment, text=option, variable=self.payment_right, value=option)
            rb.pack(side=LEFT, padx=5)
            

        self.ce50 = Button(self.booking_window, text="PAYMENT", command=self.check_payment, font=('Dotum', 14, 'bold'), bg="#007BFF", fg="black", bd=5, width=10, height=2)
        self.ce50.place(relx=0.5, rely=0.9, anchor=CENTER)

        ce60 = Button(self.booking_window, text="<<", command=self.ask_leave, font=('Dotum', 10))
        ce60.pack(side="left")
        
    def ask_leave(self):
        if messagebox.askokcancel("Peringatan", "Apakah Anda Yakin Ingin Meninggalkan Halaman Ini?"):
           self.booking_window.destroy() 
        
    def check_payment(self):
        # Check if all fields are filled
        if (self.pemesan_name.get() == "" or
            self.identitas_type.get() == "0" or
            self.identitas_number.get() == "" or
            self.birthdate_dd.get() == "" or
            self.birthdate_mm.get() == "" or
            self.birthdate_yy.get() == "" or
            self.gender.get() == "0" or
            self.phone_number_right.get() == "" or
            self.email_right.get() == "" or
            self.checkin_dd.get() == "" or
            self.checkin_mm.get() == "" or
            self.checkin_yy.get() == "" or
            self.checkout_dd.get() == "" or
            self.checkout_mm.get() == "" or
            self.checkout_yy.get() == "" or
            self.room_type.get() == "" or
            self.payment_right.get() == "0"):
            messagebox.showerror("Peringatan", "Pastikan Untuk Mengisi Semua Form Dengan Benar")
        elif not self.validate_email():
            messagebox.showerror("Error", "Email harus mengandung simbol '@'")
        elif len(self.identitas_number.get()) != 16:
            messagebox.showerror("Error", "Nomor Identitas harus 16 digit.")
        elif len(self.phone_number_right.get()) < 10:
            messagebox.showerror("Error", "Nomor Telepon harus minimal 10 digit.")
        else:
            hasil = messagebox.askokcancel("Success", "Data telah berhasil diisi, Apakah Anda ingin melanjutkan ke proses pembayaran?")
            if hasil:
                self.payment_tamu()

    def validate_email(self):
        email = self.email_right.get()
        if '@' not in email and email != "":
            return False
        return True
                

    def payment_tamu(self):
        self.payment_tamu_window = Toplevel(self.root)
        self.payment_tamu_window.geometry("1920x1080")
        self.payment_tamu_window.title("PEMBAYARAN")
        self.payment_tamu_window.configure(bg="#F0F0FF")

        i51 = Label(self.payment_tamu_window, text="SANDYA", bg="#83838B", fg="white", font=('Dotum', 25))
        i52 = Label(self.payment_tamu_window, text="Hotels-Resorts-Spas", fg="white", bg="#83838B", font=('Dotum', 12))
        i51.pack(fill="x")
        i52.pack(fill="x")

        # Create a frame to display the user's data
        receipt_frame = Frame(self.payment_tamu_window, bg="#F0F0FF")
        receipt_frame.pack(pady=20)

        # Get the data from the booking form
        pemesan_name = self.pemesan_name.get()
        identitas_type = self.identitas_type.get()
        identitas_number = self.identitas_number.get()
        birthdate = f"{self.birthdate_dd.get()}/{self.birthdate_mm.get()}/{self.birthdate_yy.get()}"
        gender = self.gender.get()
        address = self.text_address.get("1.0", "end-1c")
        phone_number = self.phone_number_right.get()
        email = self.email_right.get()
        checkin = f"{self.checkin_dd.get()} / {self.checkin_mm.get()} / {self.checkin_yy.get()}"
        checkout = f"{self.checkout_dd.get()} / {self.checkout_mm.get()} / {self.checkout_yy.get()}"
        room_type = self.room_type.get()
        payment_method = self.payment_right.get()
        
        self.order_number = StringVar()
        self.kode_pin = StringVar()

        a = Label(self.payment_tamu_window, bg="#F0F0FF", bd=10, relief=RIDGE, highlightbackground="white", highlightthickness=2)
        a.place(relx=0.40, rely=0.263, relheight=0.67, relwidth=0.47)

        a = Label(self.payment_tamu_window, bd=2, relief=RIDGE)
        a.place(relx=0.40, rely=0.263, relheight=0.670, relwidth=0.47)

        label_frame_right = Frame(a)
        label_frame_right.pack(pady=8, fill="x")

        # Create a label to display the user's data
        user_data_label = Label(label_frame_right, font=('Dotum', 12, 'bold'), fg="white")
        user_data_label.pack(pady=10, fill="x")

        # Create a title label
        title_label = Label(user_data_label, text="", font=('Dotum', 18, 'bold'), fg="white")
        title_label.pack(pady=10)

        image = Image.open("HE.jpg")
        test = ImageTk.PhotoImage(image)
        labell = Label(self.payment_tamu_window, image=test)
        labell.image = test
        labell.place(x=577, y=95)

        image = Image.open("qris.png")
        test = ImageTk.PhotoImage(image)
        labell = Label(self.payment_tamu_window, image=test)
        labell.image = test
        labell.place(x=213, y=230)

        print_button = Button(self.payment_tamu_window, text="ALREADY PAID", command=lambda: self.print_receipt(user_data_label.cget("text")), font=('Dotum', 12, 'bold'), bg="#007BFF", fg="BLACK", bd=5, width=15, height=2)
        print_button.place(x=270, y=640)  

        ce65 = Button(self.payment_tamu_window, text="<<", command=self.ask_leave_payment, font=('Dotum', 10))
        ce65.pack(side="left")

        
        # Create a frame to hold the user's data
        data_frame = Frame(user_data_label)
        data_frame.pack(pady=10, fill="x")
  
        # Create labels to display the user's data
        self.order_number = f"SY-{ ''.join(random.choice(string.ascii_uppercase) for _ in range(6)) }-{random.randint(1, 1000):03d}"
        order_number_label = tk.Label(data_frame, text=f"  NO. ORDER :  {self.order_number}", font=('Dotum', 30, 'bold'), fg="#999999")
        order_number_label.grid(row=0, column=0, sticky="w", pady=(0, 3))

        self.kode_pin = str(random.randint(100000, 999999))

        checkout_day = int(self.checkout_dd.get())
        checkout_month = int(self.checkout_mm.get())
        checkout_year = int(self.checkout_yy.get())

        checkout_date = datetime.date(checkout_year, checkout_month, checkout_day)
        today = datetime.date.today()

        jumlah_hari = (checkout_date - today).days

        if jumlah_hari == 0:
            jumlah_hari = 1
            
        room_type = self.room_type.get()
        prices = {
            "Standard ( Rp139.060,00 )": 139060,
            "Superior ( Rp165.368,00 )": 165368,
            "Suite ( Rp171.982,00 )": 171982,
            "Presidential ( Rp648.241,00 )": 648241
        }

        total_pembayaran = jumlah_hari * prices[room_type]


        Label(data_frame, text=f"    Nama Pemesan    : {pemesan_name}", font=('Dotum', 16, 'bold'), fg="white").grid(row=1, column=0, sticky="w", pady=(5, 5))

        Label(data_frame, text=f"    Jenis Kelamin       : {gender}", font=('Dotum', 16, 'bold'), fg="white").grid(row=2, column=0, sticky="w", pady=(5, 5))

        Label(data_frame, text=f"    Alamat                     : {address}", font=('Dotum', 16, 'bold'), fg="white").grid(row=3, column=0, sticky="w", pady=(5, 5))
     
        Label(data_frame, text=f"    No. Telepon           : {phone_number}", font=('Dotum', 16, 'bold'), fg="white").grid(row=4, column=0, sticky="w", pady=(5, 5))
     
        Label(data_frame, text=f"    E-mail                      : {email}", font=('Dotum', 16, 'bold'), fg="white").grid(row=5, column=0, sticky="w", pady=(5, 5))
     
        Label(data_frame, text=f"   ================================================================================== ", font=('Dotum', 11, 'bold'), fg="white").grid(row=6, column=0, sticky="w", pady=(5, 5))

        Label(data_frame, text=f"   Check-in                        : {checkin}", font=('Dotum', 14), fg="white").grid(row=7, column=0, sticky="w", pady=(0, 0))

        Label(data_frame, text=f"   Check-out                     : {checkout}", font=('Dotum', 14), fg="white").grid(row=8, column=0, sticky="w", pady=(0, 0))

        Label(data_frame, text=f"   Jumlah hari                    : {jumlah_hari} hari", font=('Dotum', 14), fg="white").grid(row=9, column=0, sticky="w", pady=(0, 0))

        Label(data_frame, text=f"   Tipe Kamar                    : {room_type}", font=('Dotum', 14), fg="white").grid(row=10, column=0, sticky="w", pady=(0, 0))
    
        Label(data_frame, text=f"   Metode Pembayaran    : {payment_method}", font=('Dotum', 14), fg="white").grid(row=11, column=0, sticky="w", pady=(0,0))

        Label(data_frame, text=f"   ================================================================================== ", font=('Dotum', 12, 'bold'), fg="white").grid(row=12, column=0, sticky="w", pady=(5, 0))

        Label(data_frame, text=f"   Total Pembayaran   : Rp{total_pembayaran:,.2f}  ", font=('Dotum', 16, 'bold'), fg="white").grid(row=13, column=0, sticky="w", pady=(5, 5))
  
        Label(data_frame, text="                               Contact Number: +66 2 365 9110    |    Email us: reservesandya@sandya.com    |    web : www.sandyahotels.com", font=('Dotum', 9, 'bold'), fg="white").grid(row=14, column=0, sticky="w", pady=(42, 0))
        

    def ask_leave_payment(self):
        if messagebox.askokcancel("Peringatan", "Apakah Anda Yakin Ingin Meninggalkan Halaman Ini?"):
           self.payment_tamu_window.destroy() 

    def print_receipt(self, user_data):
        # Create a loading window
        loading_window = Toplevel(self.payment_tamu_window)
        loading_window.title("Loading...")
        loading_window.geometry("250x150")  # Increased size to make it more visible

        # Set a background color for the loading window
        loading_window.configure(background="#f0f0f0")  # Light gray background

        # Create a progress bar
        progress_bar = ttk.Progressbar(loading_window, orient="horizontal", length=200, mode="indeterminate")
        progress_bar.pack(pady=20)

        loading_window.geometry("300x100+{}+{}".format(int((loading_window.winfo_screenwidth()-300)/2), int((loading_window.winfo_screenheight()-100)/2)))
        loading_label = Label(loading_window, text="Memproses Pembayaran...", font=('Helvetica', 18, 'bold italic'), fg="#000", bg="#f0f0f0")
        loading_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Start the progress bar
        progress_bar.start()

        # Show the loading window for 3 seconds
        def close_loading_window():
            loading_window.destroy()
            self.show_success_message()

        loading_window.after(3500, close_loading_window)

        # Make sure the loading window is on top of the main window
        loading_window.transient(self.payment_tamu_window)
        loading_window.grab_set()

    def show_success_message(self):
        messagebox.showinfo("Success", "Pembayaran berhasil!")
        self.kode_kamar()


    def kode_kamar(self):
        self.kode_kamar_window = Toplevel(self.root)
        self.kode_kamar_window.geometry("1920x1080")
        self.kode_kamar_window.title("KODE KAMAR")
        self.kode_kamar_window.configure(bg="#F0F0FF")

        i51 = Label(self.kode_kamar_window, text="SANDYA", bg="#83838B", fg="white", font=('Dotum', 25))
        i52 = Label(self.kode_kamar_window, text="Hotels-Resorts-Spas", fg="white", bg="#83838B", font=('Dotum', 12))
        i51.pack(fill="x")
        i52.pack(fill="x")

        a = Label(self.kode_kamar_window, bg="#964B00", bd=10, relief=RIDGE, highlightbackground="white", highlightthickness=2)
        a.place(relx=0.26, rely=0.135, relheight=0.72, relwidth=0.52)

        a = Label(self.kode_kamar_window, bd=2, relief=RIDGE)
        a.place(relx=0.26, rely=0.135, relheight=0.72, relwidth=0.52)


        image = Image.open("kode kamar.jpg")
        test = ImageTk.PhotoImage(image)
        labell1 = Label(self.kode_kamar_window, image=test)
        labell1.image = test
        labell1.place(x=580, y=295)
        
        label_frame_right = Frame(a)
        label_frame_right.pack(pady=8, fill="x")

        kode_kamar_label = Label(label_frame_right, font=('Dotum', 12, 'bold'), fg="white")
        kode_kamar_label.pack(pady=10, fill="x")

        # Create a frame to hold the user's data
        kamar_frame = Frame(kode_kamar_label)
        kamar_frame.pack(pady=10, fill="x")

        pemesan_name = self.pemesan_name.get()
        lantai = random.randint(1, 8)
        self.kode_pin = str(random.randint(100000, 999999))
        nomor_kamar = str(random.randint(100, 999))

        label_text = Label(self.kode_kamar_window, text=f"Lt. {lantai} ", font=('Dotum', 14, 'bold'), fg="#8B0A1A", bg="white")
        label_text.place(x=777, y=350)

        label_text = Label(self.kode_kamar_window, text=f"Kamar {nomor_kamar} ", font=('Dotum', 14, 'bold'), fg="#8B0A1A", bg="white")
        label_text.place(x=777, y=395)

        label_text = Label(self.kode_kamar_window, text=f"PIN {self.kode_pin} ", font=('Dotum', 14, 'bold'), fg="#8B0A1A", bg="white")
        label_text.place(x=777, y=440)

        order_number_label = Label(kamar_frame, text=f"  NO. ORDER :  {self.order_number}", font=('Dotum', 30, 'bold'), fg="#999999")
        order_number_label.grid(row=0, column=0, sticky="w", pady=(0, 10))

        Label(kamar_frame, text=f"     Hi, {pemesan_name} ", font=('Dotum', 16, 'bold'), fg="white").grid(row=1, column=0, sticky="w", pady=(5, 5))

        Label(kamar_frame, text="      Terima kasih telah memilih untuk menginap di Sandya Hotels-Resorts-Spas. Kami sangat senang menyambut Anda ", font=('Dotum', 11), fg="white").grid(row=2, column=0, sticky="w", pady=(5, 3))

        Label(kamar_frame, text="      di hotel kami. Berikut adalah rincian reservasi Anda : ", font=('Dotum', 11), fg="white").grid(row=3, column=0, sticky="w", pady=(0, 10))

        Label(kamar_frame, text=f"     Silakan menuju ke lantai {lantai} ke nomor kamar {nomor_kamar} menggunakan lift yang berada di sebelah kanan lobby. ", font=('Dotum', 11), fg="white").grid(row=5, column=0, sticky="w", pady=(260, 3))

        Label(kamar_frame, text=f"     Untuk masuk ke kamar Anda, silakan masukkan kode pin {self.kode_pin} pada panel kunci elektronik yang terdapat di pintu kamar ", font=('Dotum', 11),fg="white").grid(row=13, column=0, sticky="w", pady=(0, 3))

        Label(kamar_frame, text="      Pastikan Anda memasukkan kode dengan benar dan tunggu hingga lampu hijau menyala sebelum membuka pintu. ", font=('Dotum', 11), fg="white").grid(row=14, column=0, sticky="w", pady=(0, 3))
        
        Label(kamar_frame, text="      Kami berharap Anda menikmati masa tinggal Anda bersama kami. Jika Anda memerlukan bantuan atau informasi tambahan, ", font=('Dotum', 11), fg="white").grid(row=15, column=0, sticky="w", pady=(0, 3))

        Label(kamar_frame, text="      jangan ragu untuk menghubungi resepsionis kami yang siap melayani Anda 24 jam. ", font=('Dotum', 11), fg="white").grid(row=16, column=0, sticky="w", pady=(0, 0))

        Label(kamar_frame, text="                                       Contact Number: +66 2 365 9110    |    Email us: reservesandya@sandya.com    |    web : www.reservewandya.com", font=('Dotum', 9, 'bold'), fg="white").grid(row=17, column=0, sticky="w", pady=(39, 0))


        self.ce57 = Button(self.kode_kamar_window, text="CLOSE", command=lambda: [self.kode_kamar_window.destroy(), self.root.deiconify()], font=('Dotum', 14, 'bold'), bg="#007BFF", fg="black", bd=5, width=10, height=2)
        self.ce57.place(relx=0.5, rely=0.9, anchor=CENTER)
            

    def open_login_page(self):
        self.login_window = Toplevel(self.root)
        self.login_window.geometry("1920x1080")
        self.login_window.title("CHECKOUT")
        self.login_window.configure(bg="#F0F0FF")

        image = Image.open("checkout.jpg")
        test = ImageTk.PhotoImage(image)
        labell = Label(self.login_window, image=test)
        labell.image = test
        labell.place(x=0, y=0)

         # Create a frame for the title and label
        title_frame = Frame(self.login_window)
        title_frame.pack(pady=83)

        i47 = Label(self.login_window, text="SANDYA", bg="#83838B", fg="white", font=('Dotum', 25))
        i48 = Label(self.login_window, text="Hotels-Resorts-Spas", fg="white", bg="#83838B", font=('Dotum', 12))
        i47.pack(fill="x")
        i48.pack(fill="x")
        
        a = Label(self.login_window, bg="#964B00", bd=10, relief=RIDGE, highlightbackground="white", highlightthickness=2)
        a.place(relx=0.31, rely=0.350, relheight=0.26, relwidth=0.38)

        a = Label(self.login_window, bd=2, relief=RIDGE)
        a.place(relx=0.31, rely=0.350, relheight=0.26, relwidth=0.38)
        
        label_frame_right = Frame(a)
        label_frame_right.pack(pady=8, fill="x")

        login_window_label = Label(label_frame_right, font=('Dotum', 12, 'bold'), fg="white")
        login_window_label.pack(pady=10, fill="x")

        # Create a frame to hold the user's data
        login_frame = Frame(login_window_label)
        login_frame.pack(pady=10, fill="x")


        self.order_number = StringVar()
        self.kode_pin = StringVar()

        Label(login_frame, text="NO. ORDER", font=('Dotum', 14,'bold')).grid(row=0, column=0, padx=50, pady=10, sticky='w')
        self.entry_order_number = Entry(login_frame, bd=5, textvar=self.order_number, width=30, font=('Dotum', 14))
        self.entry_order_number.grid(row=0, column=1, padx=10, pady=10)

        Label(login_frame, text="PIN PINTU", font=('Dotum', 14,'bold')).grid(row=1, column=0, padx=50, pady=10, sticky='w')
        self.entry_kode_pin = Entry(login_frame, bd=5, show='*', textvar=self.kode_pin, width=30, font=('Dotum', 14))
        self.entry_kode_pin.grid(row=1, column=1, padx=10, pady=10)

        self.order_number.trace("w", lambda *args: self.order_number.set(self.order_number.get().upper()))
        
        ce37 = Button(self.login_window, text="CHECK OUT", command=self.checkout_and_book, font=('Dotum', 14, 'bold'), bg="#007BFF", fg="black", bd=5, width=10, height=2)
        ce37.pack(side=BOTTOM, pady=95)

        ce65 = Button(self.login_window, text="<<", command=self.ask_leave_checkout, font=('Dotum', 10))
        ce65.pack(side="left") 

    def ask_leave_checkout(self):
        if messagebox.askokcancel("Peringatan", "Apakah Anda Yakin Ingin Meninggalkan Halaman Ini?"):
           self.login_window.destroy()

    def checkout_and_book(self):
        nomor_order = self.order_number.get()
        kode_pin = self.kode_pin.get()

        # Periksa apakah semua bidang telah diisi
        if not all([nomor_order, kode_pin]): 
            messagebox.showerror("Error", "Harap isi semua bidang!")
        else:
            self.loading_window(None)  # Call the loading window function

    def loading_window(self, user_data):
        # Create a loading window
        loading_window = Toplevel(self.login_window)
        loading_window.title("Loading...")
        loading_window.geometry("250x150")  # Increased size to make it more visible

        # Set a background color for the loading window
        loading_window.configure(background="#f0f0f0")  # Light gray background

        # Create a progress bar
        progress_bar = ttk.Progressbar(loading_window, orient="horizontal", length=200, mode="indeterminate")
        progress_bar.pack(pady=20)

        loading_window.geometry("300x100+{}+{}".format(int((loading_window.winfo_screenwidth()-300)/2), int((loading_window.winfo_screenheight()-100)/2)))
        loading_label = Label(loading_window, text="Memproses Checkout...", font=('Helvetica', 18, 'bold italic'), fg="#000", bg="#f0f0f0")
        loading_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Start the progress bar
        progress_bar.start()

          # Show the loading window for 3 seconds
        def close_loading_window():
            loading_window.destroy()
            self.show_success_message_checkout()

        loading_window.after(3500, close_loading_window)

        # Make sure the loading window is on top of the main window
        loading_window.transient(self.login_window)
        loading_window.grab_set()

    def show_success_message_checkout(self):
        if len(self.order_number.get()) < 13:
                messagebox.showerror("Error", "Check Out Gagal! Harap Masukkan NO Order dan Pin Pintu Dengan Benar")
        else:
            messagebox.showinfo("Success", "Anda Telah Berhasil Check Out! Terima kasih Atas Kepercayaan Anda Kepada Sandya hotels-resorts-spas. Kami Berharap Dapat Melayani Anda Kembali!")
            self.login_window.destroy()  # Destroy the login window here

    def open_signup_page(self):
        self.open_hotel_log_page()
    
    def get_pemesan_name(self):
        return self.pemesan_name.get()

    def get_address(self):
        return self.text_address.get("1.0", "end-1c")

    def get_check_in_date(self):
        return self.checkin_right.get()

    def get_check_out_date(self):
        return self.checkout_right.get()

class HotelReservationController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_controller(self)

    def login(self):
        order_number = self.view.order_number()
        pin_kode = self.kode_pin()
        if order_number and pin_kode:
            self.view.open_hotel_log_page()
        else:
            self.view.show_message("Please enter order number and pin code.", False)
    
    def open_hotel_log_page(self):
        self.view.open_hotel_log_page()

    def open_hotel_log_page_A(self):
        self.view.open_hotel_log_page_A(self.view.hotel_log_window)

    def open_booking_page(self,previous_window):
        self.view.create_widgets()
        self.view.root.mainloop()


           
if __name__ == "__main__":
    app = HotelReservationView()
   