import os
import customtkinter
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from tkinter import ttk
import struct
# Define class for Book
class Book:
    def __init__(self, barcode, bookname, author, publishing_house, release_date, inventory):
        self.barcode = barcode
        self.bookname = bookname
        self.author = author
        self.publishing_house = publishing_house
        self.release_date = release_date
        self.inventory = inventory

#FUNCTION FOR MEMBERS
class Member:
 def __init__(self, i_n, name_surname, birthdate, phone_number, address, situation):
        self.i_n = i_n
        self.name_surname = name_surname
        self.birthdate = birthdate
        self.phone_number = phone_number
        self.address = address
        self.situation = situation

# Define class for Borrowed
class Borrowed:
    def __init__(self, memberi_n, book_barcode, to_use, day_of_use, delay_days, situation):
        self.memberi_n = memberi_n
        self.book_barcode = book_barcode
        self.to_use = to_use
        self.day_of_use = day_of_use
        self.delay_days = delay_days
        self.situation = situation


# Function to add a book
def add_book_interface():
    # Function to handle book addition
    def add_book():
        barcode = barcode_entry.get()
        bookname = bookname_entry.get()
        author = author_entry.get()
        publishing_house = publishing_house_entry.get()
        release_date = release_date_entry.get()
        inventory = inventory_entry.get()
        
        with open("Books.data", "a") as file:
            file.write(f"{barcode},{bookname},{author},{publishing_house},{release_date},{inventory}\n")
        
        messagebox.showinfo("Success", "Book registration completed.")
        add_book_window.destroy()

    # Create the book addition interface
    add_book_window = tk.Tk()
    add_book_window.geometry("300x300")
    add_book_window.configure(bg="#202227")
    add_book_window.title("Add Book")

    tk.Label(add_book_window, text="Barcode Number:", bg="#202227", fg="#f4f4f4").grid(padx=10,pady=10,row=0, column=0)
    barcode_entry = tk.Entry(add_book_window)
    barcode_entry.grid(row=0, column=1)

    tk.Label(add_book_window, text="Book Title:", bg="#202227", fg="#f4f4f4").grid(padx=10,pady=10,row=1, column=0)
    bookname_entry = tk.Entry(add_book_window)
    bookname_entry.grid(row=1, column=1)

    tk.Label(add_book_window, text="Author:", bg="#202227", fg="#f4f4f4").grid(padx=10,pady=10,row=2, column=0)
    author_entry = tk.Entry(add_book_window)
    author_entry.grid(row=2, column=1)

    tk.Label(add_book_window, text="Publishing House:", bg="#202227", fg="#f4f4f4").grid(padx=10,pady=10,row=3, column=0)
    publishing_house_entry = tk.Entry(add_book_window)
    publishing_house_entry.grid(row=3, column=1)

    tk.Label(add_book_window, text="Release Date:", bg="#202227", fg="#f4f4f4").grid(padx=10,pady=10,row=4, column=0)
    release_date_entry = tk.Entry(add_book_window)
    release_date_entry.grid(row=4, column=1)

    tk.Label(add_book_window, text="Inventory:", bg="#202227", fg="#f4f4f4").grid(padx=10,pady=10,row=5, column=0)
    inventory_entry = tk.Entry(add_book_window)
    inventory_entry.grid(row=5, column=1)

    add_button = tk.Button(add_book_window, text="Add Book", command=add_book, bg="#18a0fb", fg="#f4f4f4")
    add_button.grid(row=6, columnspan=2)

    add_book_window.mainloop()

# Function to delete a book
def delete_book_interface():
    # Function to handle book deletion
    def delete_book():
        Book.barcode = bbarcode_entry.get()
        result = 0
        try:
            with open("Books.data", "r") as file:
                lines = file.readlines()
            with open("backup.data", "w") as new_file:
                for line in lines:
                    if str(Book.barcode) not in line:
                        new_file.write(line)
                    else:
                        result = 1
            if result == 0:
                messagebox.showerror("Error", f"{Book.barcode} BOOK WITH BARCODE NUMBER NOT FOUND.")
            else:
                os.remove("Books.data")
                os.rename("backup.data", "Books.data")
                messagebox.showinfo("Success", f"{Book.barcode} BOOK WITH BARCODE NUMBER DELETED.")
                delete_book_window.destroy()
        except FileNotFoundError:
            messagebox.showerror("Error", "Books.data file not found.")

    # Create the book deletion interface
    delete_book_window = tk.Tk()
    delete_book_window.geometry("300x130")
    delete_book_window.configure(bg="#202227")
    delete_book_window.title("Delete Book")

    tk.Label(delete_book_window, text="Barcode Number:", bg="#202227", fg="#f4f4f4").grid(padx=20,pady=20,row=0, column=0)
    bbarcode_entry = tk.Entry(delete_book_window)
    bbarcode_entry.grid(row=0, column=1)

    delete_button = tk.Button(delete_book_window, text="Delete Book", command=delete_book, bg="#18a0fb", fg="#f4f4f4")
    delete_button.grid(row=1, columnspan=2,padx=20,pady=20)

    delete_book_window.mainloop()

# Function for book transactions menu
def book_transactions():
    def handle_book_transactions():
        window.destroy()  # Close the current window
        add_book_interface()

    def handle_member_transactions():
        window.destroy()  
        delete_book_interface()

    def handle_borrowing_procedures():
        window.destroy()  
        book_list_interface()
    
    
    window = tk.Tk()
    window.geometry("850x400")
    window.title("Library Management System")
    window.configure(bg="#202227")
    
    tk.Label(window, text="Book Transactions", font=('Arial',18), bg="#202227", fg="#f4f4f4").pack(padx=20,pady=40)
    Label = tk.Label(window, text="explore categories ↓",font=('Arial',10), bg="#202227", fg="#f4f4f4").pack(padx=20,pady=20,anchor="nw")

    tk.Button(window, text="ADD BOOK", command=add_book_interface,width=20, height=7, bg="#18a0fb", fg="#f4f4f4").pack(side=tk.LEFT,padx=20,pady=20)
    tk.Button(window, text="DELETE BOOK", command=delete_book_interface,width=20, height=7, bg="#18a0fb", fg="#f4f4f4").pack(side=tk.LEFT,padx=20,pady=20)
    tk.Button(window, text="LIST BOOKS", command=book_list_interface,width=20, height=7, bg="#18a0fb", fg="#f4f4f4").pack(side=tk.LEFT,padx=20,pady=20)
    tk.Button(window, text="BACK TO MAIN MENU", command=window.destroy,width=20, height=7, bg="#18a0fb", fg="#f4f4f4").pack(side=tk.LEFT,padx=20,pady=20)

    window.mainloop()

# Function to list books
def book_list_interface():
 def load_books_from_file():
     try:
        with open("Books.data", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 6:
                    tree.insert('', 'end', values=(data[0], data[1], data[2], data[3],data[4],data[5]))
     except FileNotFoundError:
         messagebox.showerror("Error", "Books.data file not found.")

 # Create main window
 root = tk.Tk()
 root.title("Kitap Listesi")
 # Stil oluştur
 style = ttk.Style(root)
 style.theme_use("clam")

 # Treeview stilini ayarla
 style.configure("Treeview",
                background="#202227",
                foreground="white",
                fieldbackground="#202227",
                rowheight=25,
                font=('Arial', 12))

 style.map('Treeview', background=[('selected', 'blue')])

 # Treeview başlık stilini ayarla
 style.configure("Treeview.Heading",
                background="black",
                foreground="white",
                font=('Arial', 12, 'bold'))
 # Create treeview
 tree = ttk.Treeview(root, columns=('BOOK-BARCODE', 'BOOK-NAME', 'BOOK-AUTHOR', 'BOOK-PUBLISHER','BOOK-PUBLICATION DATE','BOOK-STOCK'), show='headings')
 tree.heading('BOOK-BARCODE', text='BOOK-BARCODE')
 tree.heading('BOOK-NAME', text='BOOK-NAME')
 tree.heading('BOOK-AUTHOR', text='BOOK-AUTHOR')
 tree.heading('BOOK-PUBLISHER', text='BOOK-PUBLISHER')
 tree.heading('BOOK-PUBLICATION DATE',text='BOOK-PUBLICATION DATE')
 tree.heading('BOOK-STOCK',text='BOOK-STOCK')
 tree.pack(pady=10,padx=10)

 # Load books from file when the program starts
 load_books_from_file()

 root.mainloop()
# Function for adding a member
def add_member():
    def register_member():
        # Retrieve data from entry fields
        i_n = id_entry.get()
        name_surname = name_surname_entry.get()
        birthdate = birthdate_entry.get()
        phone_number = phone_number_entry.get()
        address = address_entry.get()
        situation = 0
        
        # Write member data to file
        with open("members.data", "a") as file:
            file.write(f"{i_n},{name_surname},{birthdate},{phone_number},{address},{situation}\n")

        # Show completion message
        messagebox.showinfo("Success", "Member registration completed.")

        # Close the window after registration
        window.destroy()

    # Create the member addition interface
    window = tk.Tk()
    window.geometry("300x300")
    window.configure(bg="#202227")
    window.title("Add Member")

    tk.Label(window, text="Member's ID Number:", bg="#202227", fg="#f4f4f4").grid(padx=10,pady=15,row=0, column=0)
    id_entry = tk.Entry(window)
    id_entry.grid(row=0, column=1)

    tk.Label(window, text="Name and Surname:", bg="#202227", fg="#f4f4f4").grid(padx=10,pady=15,row=1, column=0)
    name_surname_entry = tk.Entry(window)
    name_surname_entry.grid(row=1, column=1)

    tk.Label(window, text="Date of Birth:", bg="#202227", fg="#f4f4f4").grid(padx=10,pady=15,row=2, column=0)
    birthdate_entry = tk.Entry(window)
    birthdate_entry.grid(row=2, column=1)

    tk.Label(window, text="Telephone Number:", bg="#202227", fg="#f4f4f4").grid(padx=10,pady=15,row=3, column=0)
    phone_number_entry = tk.Entry(window)
    phone_number_entry.grid(row=3, column=1)

    tk.Label(window, text="Address:", bg="#202227", fg="#f4f4f4").grid(padx=10,pady=15,row=4, column=0)
    address_entry = tk.Entry(window)
    address_entry.grid(row=4, column=1)

    tk.Button(window, text="Add Member", command=register_member, bg="#18a0fb", fg="#f4f4f4").grid(row=5, column=0, columnspan=2)

    window.mainloop()

def delete_member():
    def confirm_deletion():
        i_n = id_entry.get()
        result = 0
        try:
            with open("members.data", "r") as file:
                lines = file.readlines()
            with open("backup.data", "w") as new_file:
                for line in lines:
                    if i_n not in line:
                        new_file.write(line)
                    else:
                        result = 1
            if result == 0:
                messagebox.showwarning("Warning", f"{i_n} No member with ID number found.")
            else:
                os.remove("members.data")
                os.rename("backup.data", "members.data")
                messagebox.showinfo("Success", f"{i_n} Member with ID number deleted.")
                window.destroy()
        except FileNotFoundError:
            messagebox.showerror("Error", "members.data file not found.")

    window = tk.Tk()
    window.geometry("350x150")
    window.configure(bg="#202227")
    window.title("Delete Member")

    tk.Label(window, text="ID Number of the Member:", bg="#202227", fg="#f4f4f4").grid(padx=20,pady=20,row=0, column=0)
    id_entry = tk.Entry(window)
    id_entry.grid(row=0, column=1)

    delete_button = tk.Button(window, text="Delete Member", command=confirm_deletion, bg="#18a0fb", fg="#f4f4f4")
    delete_button.grid(row=1, column=0, columnspan=2,padx=20,pady=20)

    window.mainloop()

def member_list():
    def load_books_from_file():
     try:
        with open("members.data", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 6:
                    tree.insert('', 'end', values=(data[0], data[1], data[2], data[3],data[4],data[5]))
     except FileNotFoundError:
         print("Error", "members.data file not found.")

    # Create main window
    root = tk.Tk()
    root.title("Member List")
    # Stil oluştur
    style = ttk.Style(root)
    style.theme_use("clam")

    # Treeview stilini ayarla
    style.configure("Treeview",
                background="#202227",
                foreground="white",
                fieldbackground="#202227",
                rowheight=25,
                font=('Arial', 12))

    style.map('Treeview', background=[('selected', 'blue')])
    # Treeview başlık stilini ayarla
    style.configure("Treeview.Heading",
                background="black",
                foreground="white",
                font=('Arial', 12, 'bold'))
    # Create treeview
    tree = ttk.Treeview(root, columns=('MEMBER ID', 'MEMBER NAME-SURNAME', 'MEMBER DATE OF BIRTH', 'MEMBER PHONE NUMBER','MEMBER ADDRESS','MEMBER SITUATION'), show='headings')
    tree.heading('MEMBER ID', text='MEMBER IDENTIFICATION NO')
    tree.heading('MEMBER NAME-SURNAME', text='MEMBER NAME-SURNAME')
    tree.heading('MEMBER DATE OF BIRTH', text='MEMBER DATE OF BIRTH')
    tree.heading('MEMBER PHONE NUMBER', text='MEMBER PHONE NUMBER')
    tree.heading('MEMBER ADDRESS',text='MEMBER ADDRESS')
    tree.heading('MEMBER SITUATION',text='MEMBER SITUATION')
    tree.pack(pady=10,padx=10)

    # Load books from file when the program starts
    load_books_from_file()

    root.mainloop()

def member_transactions():
    def handle_book_transactions():
        window.destroy()  # Close the current window
        add_member()

    def handle_member_transactions():
        window.destroy()  
        delete_member()

    def handle_borrowing_procedures():
        window.destroy()  
        member_list()

    window = tk.Tk()
    window.geometry("850x450")
    window.configure(bg="#202227")
    window.title("Member Transactions")

    tk.Label(window, text="MEMBER TRANSACTIONS SCREEN: ", font=('Arial',18), bg="#202227", fg="#f4f4f4").pack(padx=20,pady=40)

    tk.Button(window, text="ADD MEMBER", command=add_member,width=20, height=7, bg="#18a0fb", fg="#f4f4f4").pack(side=tk.LEFT,padx=20,pady=20)
    tk.Button(window, text="DELETE MEMBER", command=delete_member,width=20, height=7, bg="#18a0fb", fg="#f4f4f4").pack(side=tk.LEFT,padx=20,pady=20)
    tk.Button(window, text="LIST MEMBERS", command=member_list,width=20, height=7, bg="#18a0fb", fg="#f4f4f4").pack(side=tk.LEFT,padx=20,pady=20)
    tk.Button(window, text="BACK TO MAIN MENU", command=window.destroy,width=20, height=7, bg="#18a0fb", fg="#f4f4f4").pack(side=tk.LEFT,padx=20,pady=20)

# Function to list borrowed books
def lend_list_interface():
    # Pencereyi oluşturma
   lend_list_window = tk.Tk()
   lend_list_window.geometry("800x450")
   lend_list_window.title("Borrowed Books List")
   lend_list_window.configure(bg="#202227")

   # Treeview için bir çerçeve oluşturma
   frame = tk.Frame(lend_list_window, bg="#202227")
   frame.pack(fill=tk.BOTH, expand=True)

   # Treeview bileşenini oluşturma
   columns = ("IDENTIFICATION NO.", "BARCODE", "GIVEN TIME")
   tree = ttk.Treeview(frame, columns=columns, show="headings")
   tree.heading("IDENTIFICATION NO.", text="IDENTIFICATION NO.")
   tree.heading("BARCODE", text="BARCODE")
   tree.heading("GIVEN TIME", text="GIVEN TIME")

   # Treeview sütun genişlikleri
   tree.column("IDENTIFICATION NO.", width=200)
   tree.column("BARCODE", width=200)
   tree.column("GIVEN TIME", width=200)

   tree.pack(fill=tk.BOTH, expand=True)

   # Dosyayı okuyup Treeview'a ekleme
   Counter = 0
   try:
      with open("lending_books.data", "r") as file:
         for line in file:
             data2 = line.strip().split(",")
             del data2[-1]
             tree.insert("", "end", values=tuple(data2))
             Counter += 1
    
       # Toplam ödünç alınan kitap sayısı
      total_label = tk.Label(lend_list_window, text="NUMBER OF BORROWED BOOKS: " + str(Counter),
                           bg="#202227", fg="#f4f4f4", font=('Arial', 9))
      total_label.pack(padx=20, pady=40)
   except FileNotFoundError:
       messagebox.showerror("Error", "lending_books.data file not found.")

     # Pencereyi çalıştırın
   lend_list_window.mainloop()


#STOCK UPDATE FUNCTION
def update_stock(barcode, number):
    try:
        with open("Books.data", "r") as file:
            lines = file.readlines()
        with open("Books.data", "w") as file:
            for line in lines:
                data = line.strip().split(",")
                if int(data[0]) == barcode:
                    data[-1] = str(int(data[-1]) + number)
                file.write(",".join(data) + "\n")
        print("STOCK UPDATED.")
    except FileNotFoundError:
        print("Books.data file not found.")

# Function to handle lending a book
def lend_book():
    # Function to handle the lending process
    def handle_lending():
        memberi_n = member_id_entry.get()
        book_barcode = int(book_barcode_entry.get())
        
        # Check if member ID exists
        uresult = 0
        try:
            with open("members.data", "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if data[0] == memberi_n:
                        uresult = 1
                        break
        except FileNotFoundError:
            messagebox.showerror("Error", "members.data file not found.")
            return

        if uresult == 0:
            messagebox.showerror("Error", f"{memberi_n} MEMBER WITH ID NUMBER NOT FOUND.")
            return

        # Check if book barcode exists
        kresult = 0
        try:
            with open("Books.data", "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if int(data[0]) == int(book_barcode):
                        kresult = 1
                        break
        except FileNotFoundError:
            messagebox.showerror("Error", "Books.data file not found.")
            return

        if kresult == 0:
            messagebox.showerror("Error", f"{book_barcode} BOOK WITH BARCODE NOT FOUND.")
            return

        # Check book stock
        if int(data[-1]) < 1:
            messagebox.showerror("Error", f"{book_barcode} THE BOOK WITH BARCODE IS OUT OF STOCK.")
            return

        to_use = to_use_entry.get()
        current_date = datetime.now()
        delivery_date = current_date.strftime("%Y-%m-%d")

        # Save lending information
        try:
            with open("lending_books.data", "a") as file:
                file.write(f"{memberi_n},{book_barcode},{to_use},{delivery_date}\n")
            messagebox.showinfo("Success", "ESCROW REGISTRATION COMPLETED.")
            update_stock(int(book_barcode), -1)
        except FileNotFoundError:
            messagebox.showerror("Error", "lending_books.data file not found.")

    # Create the lending interface
    lend_window = tk.Tk()
    lend_window.geometry("500x250")
    lend_window.configure(bg="#202227")
    lend_window.title("Book Lending")

    tk.Label(lend_window, text="MEMBER IDENTIFICATION NO.:", bg="#202227", fg="#f4f4f4").grid(padx=10,pady=10,row=0, column=0)
    member_id_entry = tk.Entry(lend_window)
    member_id_entry.grid(row=0, column=1)

    tk.Label(lend_window, text="BOOK BARCODE:", bg="#202227", fg="#f4f4f4").grid(padx=10,pady=20,row=1, column=0)
    book_barcode_entry = tk.Entry(lend_window)
    book_barcode_entry.grid(row=1, column=1)

    tk.Label(lend_window, text="HOW MANY DAYS THE MEMBER WILL USE THE BOOK:", bg="#202227", fg="#f4f4f4").grid(padx=10,pady=20,row=2, column=0)
    to_use_entry = tk.Entry(lend_window)
    to_use_entry.grid(row=2, column=1)

    lend_button = tk.Button(lend_window, text="Lend", command=handle_lending, bg="#18a0fb", fg="#f4f4f4")
    lend_button.grid(pady=20,row=3, columnspan=2)

    lend_window.mainloop()

def update_contact(i_nptr):
    result = False
    counter = 0
    members_list = []

    try:
        with open("members.data", "r+b") as file:
            while True:
                try:
                    member_obj = Member(*struct.unpack("s30s10s20s50si", file.read(116)))
                    members_list.append(member_obj)
                except struct.error:
                    break

            for member_obj in members_list:
                if member_obj.i_n == i_nptr:
                    result = True
                    break
                counter += 1

            if result:
                file.seek(counter * 116)
                member_obj.situation = -1
                file.write(struct.pack("s30s10s20s50si", member_obj.i_n.encode(), member_obj.name_surname.encode(), member_obj.birthdate.encode(), member_obj.phone_number.encode(), member_obj.address.encode(), member_obj.situation))
                print("MEMBER STATUS UPDATED.")
            else:
                print(f"No member found with ID number {i_nptr}.")

    except FileNotFoundError:
        print("members.data file not found.")

def borrow_back():
    window = tk.Tk()
    window.geometry("400x300")
    window.configure(bg="#202227")
    window.title("LOAN BOOK RETURN SCREEN")

    tk.Label(window, text="MEMBER ID NUMBER: ", bg="#202227", fg="#f4f4f4").grid(padx=20,pady=20,row=0, column=0)
    member_id_entry = tk.Entry(window)
    member_id_entry.grid(row=0, column=1)

    tk.Label(window, text="BOOK BARCODE: ", bg="#202227", fg="#f4f4f4").grid(padx=20,pady=20,row=1, column=0)
    book_barcode_entry = tk.Entry(window)
    book_barcode_entry.grid(row=1, column=1)

    def check_borrowed():
        member_id = member_id_entry.get()
        book_barcode = int(book_barcode_entry.get())
        situation=0
        uresult = 0
        delivery_date=None
        borrow_date=None
        try:
            with open("lending_books.data","r") as file:
                for line in file:
                    data=line.strip().split(",")
                    if data[0]==member_id and int(data[1])==book_barcode:
                        uresult=1
                        break
        except FileNotFoundError:
                messagebox.showerror("Error","Data file not found")
        if uresult==0:
                messagebox.showwarning("Warning", f"{member_id} WITH ID NUMBER OR {book_barcode} REGISTRATION WITH BARCODE NUMBER NOT FOUND.")
                return
        else:
            with open("lending_books.data","r") as file:
                for line in file:
                    data=line.strip().split(",")
                    if data[0] == member_id and book_barcode == int(data[1]):
                       delivery_date=data[-1]
                       break
        if delivery_date is not None:
            return_date = datetime.now()
            borrow_date = datetime.strptime(delivery_date, "%Y-%m-%d")
            days_borrowed = (return_date - borrow_date).days
            result = 0
            try:
               with open("lending_books.data", "r") as file:
                 lines = file.readlines()
               with open("new.data", "w") as new_file:
                 for line in lines:
                     if str(member_id) not in line:
                        new_file.write(line)
                     else:
                        result = 1
               if result == 0:
                    messagebox.showerror("Error", f"{member_id} BOOK WITH BARCODE NUMBER NOT FOUND.")
               else:
                  os.remove("lending_books.data")
                  os.rename("new.data", "lending_books.data")
                  messagebox.showinfo("Success", f"{member_id} BOOK WITH BARCODE NUMBER DELETED.")
            except FileNotFoundError:
                 messagebox.showerror("Error", "Books.data file not found.")
            update_stock(book_barcode,1)
            if days_borrowed>21:
                situation=-1
            else:
                situation=1

            if situation == -1:
                update_contact(member_id)
        else:
            messagebox.showerror("Warning","kayıt bulunamadı")
         

    tk.Button(window, text="Take Back", command=check_borrowed, bg="#18a0fb", fg="#f4f4f4").grid(row=3, column=0, columnspan=2,padx=20,pady=20)
    window.mainloop()

def homepage():
    def handle_book_transactions():
        windowhome.destroy()  # Close the current window
        book_transactions()

    def handle_member_transactions():
        windowhome.destroy()  
        member_transactions()

    def handle_borrowing_procedures():
        windowhome.destroy()  
        borrowed_operations()
    
    
    windowhome = tk.Tk()
    windowhome.geometry("850x500")
    windowhome.title("Library Management System")
    windowhome.configure(bg="#202227")
    
    tk.Label(windowhome, text="Library Management System", font=('Arial',18), bg="#202227", fg="#f4f4f4").pack(padx=20,pady=20,anchor="nw")
    Label = tk.Label(windowhome, text="explore categories ↓",font=('Arial',10), bg="#202227", fg="#f4f4f4").pack(padx=20,pady=20,anchor="nw")

    tk.Button(windowhome, text="Book Transactions", command=book_transactions,width=20, height=7, bg="#18a0fb", fg="#f4f4f4").pack(side=tk.LEFT,padx=20,pady=20)
    tk.Button(windowhome, text="Member Transactions", command=member_transactions,width=20, height=7, bg="#18a0fb", fg="#f4f4f4").pack(side=tk.LEFT,padx=20,pady=20)
    tk.Button(windowhome, text="Book Borrowing Procedures", command=borrowed_operations,width=20, height=7, bg="#18a0fb", fg="#f4f4f4").pack(side=tk.LEFT,padx=20,pady=20)
    tk.Button(windowhome, text="Exit", command=windowhome.destroy,width=20, height=7, bg="#18a0fb", fg="#f4f4f4").pack(side=tk.LEFT,padx=20,pady=20)

    windowhome.mainloop()

# Function for main menu
def main_menu():
    customtkinter.set_appearance_mode("System")  
    customtkinter.set_default_color_theme("blue")
    def login_event():
        if entry_1.get()=="admin" and entry_2.get()=="123": #This is just a simple demo verification,                                            
            print("Password matched!")      
            root_login.destroy() #Destroy the login window after the verification
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
            homepage() #Make the new_window
        else: #If password doesn't match
            messagebox.showerror("Login Failed", "Invalid username or password")
            entry_1.configure(text_color="red")
            entry_2.configure(text_color="red")
            print("Wrong password/username!")

    customtkinter.set_appearance_mode("dark")       
    #Define the login page window          
    root_login = customtkinter.CTk() 
    root_login.geometry(f"{500}x{500}")
    root_login.title("LOGIN PAGE")
    #Add some widgets for login page
    frame = customtkinter.CTkFrame(master=root_login,width=450, height=450, corner_radius=10)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    label_1 = customtkinter.CTkLabel(master=frame, width=400, height=120, corner_radius=10,
                                     fg_color=("gray70", "gray35"), text="Welcome to Library Automation System \n\nPlease Login! \n\nUsername=admin, Pass=123")
    label_1.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    entry_1 = customtkinter.CTkEntry(master=frame, corner_radius=20, width=400, placeholder_text="Username")
    entry_1.place(relx=0.5, rely=0.52, anchor=tk.CENTER)

    entry_2 = customtkinter.CTkEntry(master=frame, corner_radius=20, width=400, show="*", placeholder_text="Password")
    entry_2.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    button_login = customtkinter.CTkButton(master=frame, text="LOGIN", corner_radius=6, command=login_event, width=400)
    button_login.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    root_login.mainloop()



def borrowed_operations():
    
  def handle_book_transactions():
        windowt.destroy()  # Close the current window
        lend_book()
  def handle_member_transactions():
        windowt.destroy() 
        borrow_back()

  def handle_borrowing_procedures():
        windowt.destroy()  
        lend_list_interface()

  windowt = tk.Tk()
  windowt.geometry("800x400")
  windowt.title("Borrowed Book Transactions")
  windowt.configure(bg="#202227")
  tk.Label(windowt, text="LOAN BOOK TRANSACTIONS SCREEN", font=('Arial',18), bg="#202227", fg="#f4f4f4").pack(padx=20,pady=20)
  Label = tk.Label(windowt, text="explore categories ↓ ",font=('Arial',10), bg="#202227", fg="#f4f4f4").pack(padx=20,pady=20,anchor="nw")
  tk.Button(windowt, text="LEND A BOOK", command=lend_book,width=25, height=7, bg="#18a0fb", fg="#f4f4f4").pack(side=tk.LEFT,padx=20,pady=20)
  tk.Button(windowt, text="TAKE BACK THE BORROWED BOOK", command=borrow_back,width=25, height=7, bg="#18a0fb", fg="#f4f4f4").pack(side=tk.LEFT,padx=20,pady=20)
  tk.Button(windowt, text="LIST BORROWED BOOKS", command=lend_list_interface,width=25, height=7, bg="#18a0fb", fg="#f4f4f4").pack(side=tk.LEFT,padx=20,pady=20)

  windowt.mainloop()

if __name__ == "__main__":
    main_menu()

