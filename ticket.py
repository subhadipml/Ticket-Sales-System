from tkinter import *
from tkinter import messagebox
import random
from checkout import Checkout
import sqlite3
from datetime import datetime

class Ticket:
    def __init__(self, master):
        self.master = master
        master.title('Book Ticket')

        self.frame1 = Frame(master, relief='raised', borderwidth=10)
        self.frame1.pack(anchor=NW)
        self.label1 = Label(self.frame1, text='Book Your Ticket', font="Georgia 40 italic underline")
        self.label1.grid(row=0, column=0, padx=10)

        self.label2 = Label(self.frame1, text='Ticket ID(Auto Generated) : ')
        self.label2.grid(row=1, column=0)
        self.Ticket_ID = StringVar(self.frame1)
        self.Ticket_ID.set(str(random.randint(10**(10-1), 10**10-1)))
        self.label3 = Entry(self.frame1, textvariable=self.Ticket_ID)
        self.label3.grid(row=1, column=1)

        self.label4 = Label(self.frame1, text='Ticket Type : ')
        self.label4.grid(row=2, column=0)

        self.Ticket_Type = StringVar(self.frame1)  # For 1st dd
        self.Ticket_Type.set('Silver')
        self.All_Ticket_Type = {'Gold', 'Platinum'}
        self.optionmenu1 = OptionMenu(self.frame1, self.Ticket_Type, *self.All_Ticket_Type)
        self.optionmenu1.grid(row=2, column=1)

        self.label6 = Label(self.frame1, text='No. of Child($100) : ')
        self.label6.grid(row=3, column=0)
        self.child = IntVar()
        self.entry1 = Entry(self.frame1, textvariable=self.child)
        self.entry1.grid(row=3, column=1)

        self.label8 = Label(self.frame1, text='No. of Adult($200) : ')
        self.label8.grid(row=4, column=0)
        self.adult = IntVar()
        self.entry2 = Entry(self.frame1, textvariable=self.adult)
        self.entry2.grid(row=4, column=1)

        self.label10 = Label(self.frame1, text='No. of Senior($300) : ')
        self.label10.grid(row=5, column=0)
        self.senior = IntVar()
        self.entry3 = Entry(self.frame1, textvariable=self.senior)
        self.entry3.grid(row=5, column=1)

        self.Add_Ticket_button = Button(self.frame1, text="Add Ticket", command=self.add_to_cart)
        self.Add_Ticket_button.grid(row=6, column=0)

        self.Go_To_Cart_button = Button(self.frame1, text="Go To Cart", command=self.go_to_cart)
        self.Go_To_Cart_button.grid(row=6, column=1)

        self.quit_button = Button(self.frame1, text="QUIT", command=self.exit_program)
        self.quit_button.grid(row=6, column=2)

    def ticket_id(self):
        return self.Ticket_ID.get()

    def ticket_type(self):
        return self.Ticket_Type.get()

    def no_of_child(self):
        return int(self.child.get())

    def no_of_adult(self):
        return int(self.adult.get())

    def no_of_senior(self):
        return int(self.senior.get())

    def total_person(self):
        return int(self.child.get())+int(self.adult.get())+int(self.senior.get())

    def total_amount(self):
        return (int(self.child.get())*100)+(int(self.adult.get())*200)+(int(self.senior.get())*300)

    def exit_program(self):
        exit()

    def add_to_cart(self):
        con = sqlite3.connect('Tickets.db')  # dB browser for sqlite needed
        c = con.cursor()  # SQLite command, to connect to db so 'execute' method can be called
        c.execute('CREATE TABLE IF NOT EXISTS SavedTicket (TicketID TEXT, TicketType TEXT, SavedDate TEXT, NoOfChild INTEGER, NoOfAdult INTEGER, NoOfSenior INTEGER, TotalPeople INTEGER, TotalAmount INTEGER)')
        c.execute('INSERT INTO SavedTicket (TicketID, TicketType, SavedDate, NoOfChild, NoOfAdult, NoOfSenior, TotalPeople, TotalAmount) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',(self.ticket_id(), self.ticket_type(), datetime.now().strftime("%d/%m/%Y %H:%M:%S"), self.no_of_child(), self.no_of_adult(), self.no_of_senior(), self.total_person(), self.total_amount()))
        con.commit()
        con.close()

        messagebox.showinfo("Ticket Added to Cart", "Ticket added Successfully" + "\n" + "Total Amount : " + str(self.total_amount()) + "\n" + "Total People : " + str(self.total_person()))

        # Reset fields after submit
        self.Ticket_ID.set(str(random.randint(10**(10-1), 10**10-1)))
        self.Ticket_Type.set('Silver')
        self.child.set(0)
        self.adult.set(0)
        self.senior.set(0)

    def go_to_cart(self):
        self.master.destroy()
        root = Tk()
        checkout_obj = Checkout(root)
        root.mainloop()
