from tkinter import *
import ticket
import checkout
import sqlite3
from tkinter import messagebox

master = Tk()
master.title('Ticket Sales System')
master.config(bg="gold")
master.geometry("1100x600+0+0")

#---Start : Created Frame1 i.e. ( frame1 ) -----Store Infromation About Developer---#

frame1 = Frame(master, bg="gold")
frame1.pack(anchor=NW)
label1 = Label(frame1, text='Ticket Sales System', font="Georgia 60 italic underline",bg="gold")
label1.grid(row=0, column=0, padx=20, pady=10)
label2 = Label(frame1, text='About Developer', font="Courier 35 bold",bg="gold")
label2.grid(row=1, column=0, padx=5)
image1 = PhotoImage(file="img/subhadip.gif")
Label(frame1, image=image1).grid(row=2,column=0, padx=5, pady=5)
label3 = Label(frame1, text='Name : Subhadip Mondal', font="Times 30 italic",bg="gold")
label3.grid(row=3, column=0, padx=5, pady=5)
label4 = Label(frame1, text='College : Lovely Professional University', font="Times 20",bg="gold")
label4.grid(row=4, column=0, padx=5)
label5 = Label(frame1, text='Course : B.Tech(CSE)', font="Times 20",bg="gold")
label5.grid(row=5, column=0, padx=5)
label6 = Label(frame1, text= 'GitHub Repository : https://github.com/subhadipml/Ticket-Sales-System', font="halston 15 underline", fg='blue',bg="gold")
label6.grid(row=6, column=0, padx=5)
label7 = Label(frame1, text='LinkedIn ID : https://www.linkedin.com/in/subhadipml/', font="halston 15 underline", fg='blue',bg="gold")
label7.grid(row=7, column=0, padx=5)

#---End : All information about the developer---#

def ticket_booking():
    master.destroy()
    root = Tk()
    ticket_obj = ticket.Ticket(root)
    root.mainloop()
button1 = Button(frame1, text='Click To Add Ticket', font="halston 15 italic",cursor="hand2",bg="salmon", command=ticket_booking)
button1.grid(row=8, column=0, pady=5)

def go_to_cart():
    con = sqlite3.connect('Tickets.db')  # dB browser for sqlite needed
    c = con.cursor()  # SQLite command, to connect to db so 'execute' method can be called
    c.execute('CREATE TABLE IF NOT EXISTS SavedTicket (TicketID TEXT, TicketType TEXT, SavedDate TEXT, NoOfChild INTEGER, NoOfAdult INTEGER, NoOfSenior INTEGER, TotalPeople INTEGER, TotalAmount INTEGER)')
    con.commit()
    con.close()

    master.destroy()
    root = Tk()
    checkout_obj = checkout.Checkout(root)
    root.mainloop()
button2 = Button(frame1, text='Click To View Saved Ticket',font="halston 15 italic",cursor="hand2",bg="salmon", command=go_to_cart)
button2.grid(row=8, column=1, pady=5)

master.mainloop()