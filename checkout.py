from tkinter import *
import sqlite3

class Checkout:
    def __init__(self, master):
        self.master = master
        master.title('Saved Tickets')
        master.geometry('1000x600+0+0')

        self.label1 = Label(master, text='Saved Ticket List', font="Courier 20 italic")
        self.label1.place(x=10, y=0)

        self.con = sqlite3.connect('Tickets.db')  # dB browser for sqlite needed
        self.c = self.con.cursor()

        self.c.execute('SELECT * FROM SavedTicket')  # Select from which ever compound lift is selected

        self.frame = Frame(master)
        self.frame.place(x=10, y=50)

        self.Lb = Listbox(self.frame, height=5, width=80, font=("arial", 12))
        self.Lb.pack(side=LEFT, fill=Y)

        self.scroll = Scrollbar(self.frame, orient=VERTICAL)  # set scrollbar to list box for when entries exceed size of list box
        self.scroll.config(command=self.Lb.yview)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.Lb.config(yscrollcommand=self.scroll.set)

        self.Lb.insert(0, 'TicketID, TicketType, SavedDate, NoOfChild, NoOfAdult, NoOfSenior, TotalPeople, TotalAmount')  # first row in listbox

        self.data = self.c.fetchall()  # Gets the data from the table

        for row in self.data:
            r = row[0]+', '+row[1]+', '+row[2]+', '+str(row[3])+', '+str(row[4])+', '+str(row[5])+', '+str(row[6])+', '+'$'+str(row[7])
            self.Lb.insert(1, r)  # Inserts record row by row in list box
        self.con.commit()

        self.frame1 = Frame(master, bg='red')
        self.frame1.place(x=10, y=180)
        #self.Lb1 = Listbox(self.frame1, height=5, width=80, font=("arial", 12))
        #self.Lb1.pack(side=LEFT, fill=Y)

        self.label2 = Label(self.frame1, text='Book Ticket From Saved Ticket',)
        self.label2.grid(row=0, column=0)

        self.label3 = Label(self.frame1, text='Enter TicketID : ')
        self.label3.grid(row=1, column=0)
        self.Tkt_ID = StringVar(self.frame1)
        self.entry1 = Entry(self.frame1, textvariable=self.Tkt_ID)
        self.entry1.grid(row=1, column=1)
        self.label4 = Label(self.frame1, text='Enter Credit Card Details',)
        self.label4.grid(row=2, column=0)

        self.label5 = Label(self.frame1, text='Enter Customer Name : ')
        self.label5.grid(row=3, column=0)
        self.Customer_Name = StringVar(self.frame1)
        self.entry2 = Entry(self.frame1, textvariable=self.Customer_Name)
        self.entry2.grid(row=3, column=1)

        self.label6 = Label(self.frame1, text='Enter Card Number : ')
        self.label6.grid(row=4, column=0)
        self.CC_ID = IntVar(self.frame1)
        #self.Card_ID = False
        self.entry3 = Entry(self.frame1, textvariable=self.CC_ID)
        self.entry3.grid(row=4, column=1)
        self.entry3.insert(0, 'XXXXXXXXXXXXXXXX')
        self.entry3.bind("<Button>", self.cardNo)

        self.label7 = Label(self.frame1, text='Enter Month(MM) : ')
        self.label7.grid(row=5, column=0)
        self.CC_Month = IntVar(self.frame1)
        self.entry4 = Entry(self.frame1, textvariable=self.CC_Month)
        self.entry4.grid(row=5, column=1)
        self.entry4.insert(0, 'MM')
        self.entry4.bind("<Button>", self.cardMonth)

        self.label8 = Label(self.frame1, text='Enter Year(YYYY) : ')
        self.label8.grid(row=6, column=0)
        self.CC_Year = IntVar(self.frame1)
        self.entry5 = Entry(self.frame1, textvariable=self.CC_Year)
        self.entry5.grid(row=6, column=1)
        self.entry5.insert(0, 'YYYY')
        self.entry5.bind("<Button>", self.cardYear)

        self.label9 = Label(self.frame1, text='Enter CSV(XXX) : ')
        self.label9.grid(row=7, column=0)
        self.CC_CSV = IntVar(self.frame1)
        self.entry6 = Entry(self.frame1, textvariable=self.CC_CSV)
        self.entry6.grid(row=7, column=1)
        self.entry6.insert(0, 'XXX')
        self.entry6.bind("<Button>", self.cardCSV)

        self.pay = Button(self.frame1, text='Pay With Credit Card', command=self.book_now)
        self.pay.grid(row=8, column=0)

        #self.ticket_book = Button(self.frame1, text='Add More Ticket', command=self.ticket_book)
        #self.ticket_book.grid(row=8, column=1)

        self.pay = Button(self.frame1, text='QUIT', command=self.exit_program)
        self.pay.grid(row=8, column=2)

    def book_now(self):
        temp = self.entry1.get()
        self.c.execute("SELECT TicketID from SavedTicket WHERE TicketID=?", (temp,))
        data = self.c.fetchall()
        key = True
        if not data:
            key = False
        if(key == True and len(self.entry1.get())==10):
            self.c.execute('DELETE FROM SavedTicket WHERE TicketID = ' + temp)
            print('working')
            self.con.commit()
        print('hello')

    '''
    def ticket_book(self):
        self.master.destroy()
        root = Tk()
        ticket_obj = Ticket(root)
        root.mainloop()
    '''

    def exit_program(self):
        exit()

    def cardCSV(self, event):
        self.entry6.delete(0, END)

    def cardYear(self, event):
        self.entry5.delete(0, END)

    def cardMonth(self, event):
        self.entry4.delete(0, END)

    def cardNo(self, event):
        self.entry3.delete(0, END)
        #self.Card_ID = True
