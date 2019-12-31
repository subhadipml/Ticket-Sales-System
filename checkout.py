from tkinter import *
import sqlite3
from tkinter import messagebox
import random
from datetime import datetime
import sys



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

        self.label6 = Label(self.frame1, text='Enter Card Number (16 digits) : ')
        self.label6.grid(row=4, column=0)
        self.CC_ID = IntVar(self.frame1)
        #self.Card_ID = False
        self.entry3 = Entry(self.frame1, textvariable=self.CC_ID)
        self.entry3.grid(row=4, column=1)
        #self.entry3.insert(0, 'XXXXXXXXXXXXXXXX')
        #self.entry3.bind("<Button>", self.cardNo)

        self.label7 = Label(self.frame1, text='Enter Month (MM) : ')
        self.label7.grid(row=5, column=0)
        self.CC_Month = IntVar(self.frame1)
        self.entry4 = Entry(self.frame1, textvariable=self.CC_Month)
        self.entry4.grid(row=5, column=1)
        #self.entry4.insert(0, 'MM')
        #self.entry4.bind("<Button>", self.cardMonth)

        self.label8 = Label(self.frame1, text='Enter Year (YYYY) : ')
        self.label8.grid(row=6, column=0)
        self.CC_Year = IntVar(self.frame1)
        self.entry5 = Entry(self.frame1, textvariable=self.CC_Year)
        self.entry5.grid(row=6, column=1)
        #self.entry5.insert(0, 'YYYY')
        #self.entry5.bind("<Button>", self.cardYear)

        self.label9 = Label(self.frame1, text='Enter CSV (XXX) : ')
        self.label9.grid(row=7, column=0)
        self.CC_CSV = IntVar(self.frame1)
        self.entry6 = Entry(self.frame1, textvariable=self.CC_CSV)
        self.entry6.grid(row=7, column=1)
        #self.entry6.insert(0, 'XXX')
        #self.entry6.bind("<Button>", self.cardCSV)

        self.pay = Button(self.frame1, text='Pay With Credit Card', command=self.book_now)
        self.pay.grid(row=8, column=0)

        #self.ticket_book = Button(self.frame1, text='Add More Ticket', command=self.ticket_book)
        #self.ticket_book.grid(row=8, column=1)

        self.pay = Button(self.frame1, text='QUIT', command=self.exit_program)
        self.pay.grid(row=8, column=2)
        
    def book_now(self):
        try:
            temp = self.tktID()
            self.c.execute("SELECT TicketID from SavedTicket WHERE TicketID=?", (temp,))
            data = self.c.fetchall()
            key = True
            if not data:
                key = False
            if(key == True and len(temp)==10 and len(str(self.cardNo()))==16 and len(str(self.cardMonth()))==2 and len(str(self.cardYear()))==4 and len(str(self.cardCSV()))==3):
                
                t_id = "TX"+str(random.randint(10**(10-1), 10**10-1))
                messagebox.showinfo("Ticket Booked $ Print Receipt", "Ticket Booked Successfully..."+"\n"+"Transaction Receipt File : " + t_id+".pdf")
                sql_select_query = """SELECT * FROM SavedTicket WHERE TicketID = ?"""
                self.c.execute(sql_select_query, (temp,))
                row = self.c.fetchone()
                
                from reportlab.pdfgen import canvas
                import os
                from reportlab.lib.pagesizes import letter

                canvas = canvas.Canvas(t_id+".pdf", pagesize=letter)
                canvas.setLineWidth(.5)

                canvas.setFont('Helvetica', 16)
                canvas.drawString(300, 750, "Transaction Time : " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

                canvas.setFont('Courier', 30)
                canvas.drawString(370, 700, "INVOICE")

                canvas.setFont('Courier', 40)
                canvas.drawString(100, 725, "SM")
                canvas.drawString(50, 700, "Company")

                canvas.line(20, 680, 600, 680)
                canvas.setFont('Helvetica', 18)

                canvas.drawString(50, 625, "Transaction ID : " + t_id)
                canvas.drawString(50, 575, "Customer Name : " + self.custName())
                canvas.drawString(50, 525, "Ticket Type : " + row[1])
                canvas.drawString(50, 475, "Ticket ID : " + row[0])
                canvas.drawString(50, 425, "Ticket Saved Date : " + row[2])
                canvas.drawString(50, 375, "No. of Children : " + str(row[3]))
                canvas.drawString(50, 325, "No. of Adult : " + str(row[4]))
                canvas.drawString(50, 275, "No. of Senoir : " + str(row[5]))

                canvas.line(20, 200, 600, 200)
                canvas.drawString(150, 160, "Card Number : " + str(self.cardNo()))
                canvas.drawString(100, 130, "Total People")
                canvas.drawString(350, 130, "Total Amount($)")
                canvas.setFont('Courier', 25)
                canvas.drawString(100, 100, str(row[6]))
                canvas.drawString(350, 100, str(row[7]))

                canvas.line(20, 50, 600, 50)

                canvas.setFont('Helvetica', 14)
                canvas.drawString(250, 20, "***Thank You***")

                canvas.save()
                
                os.startfile(t_id+".pdf")


                self.c.execute('DELETE FROM SavedTicket WHERE TicketID = ' + temp)
                self.con.commit()

                self.master.destroy()
                root = Tk()
                ticket_obj = Checkout(root)
                root.mainloop()
            else:
                messagebox.showerror("Error", "Please Enter Valid Input!!!")
        except:
            messagebox.showerror("Error2", "Please Enter Valid Input!!!")

    '''
    def ticket_book(self):
        self.master.destroy()
        root = Tk()
        ticket_obj = Ticket(root)
        root.mainloop()
    '''

    def exit_program(self):
        sys.exit()

    def cardCSV(self):
        return int(self.CC_CSV.get())

    def cardYear(self):
        return int(self.CC_Year.get())

    def cardMonth(self):
        return int(self.CC_Month.get())

    def cardNo(self):
        return int(self.CC_ID.get())

    def custName(self):
        return self.Customer_Name.get()

    def tktID(self):
        return self.Tkt_ID.get()
