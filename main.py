
from tkinter import *
from ticket import Ticket
master = Tk()
master.title('Ticket Sales System')

#---Start : Created Frame1 i.e. ( frame1 ) -----Store Infromation About Developer---#

frame1 = Frame(master, relief='raised', borderwidth=10)
frame1.pack(anchor=NW)
label1 = Label(frame1, text='Ticket Sales System', font="Georgia 50 italic underline")
label1.grid(row=0, column=0)
label2 = Label(frame1, text='About Developer', font="Courier 20 bold")
label2.grid(row=1, column=0, padx=5, pady=5)
image1 = PhotoImage(file="img/subhadip.gif")
Label(frame1, image=image1).grid(row=2,column=0, padx=5, pady=5)
label3 = Label(frame1, text='Name : Subhadip Mondal', font="Times 20 italic")
label3.grid(row=3, column=0, padx=5, pady=5)
label4 = Label(frame1, text='College : Lovely Professional University', font="Times 10")
label4.grid(row=4, column=0, padx=5)
label5 = Label(frame1, text='Course : B.Tech(CSE)', font="Times 10")
label5.grid(row=5, column=0, padx=5)
label6 = Label(frame1, text= 'GitHub Repo : https://github.com/subhadipml/Ticket-Sales-System', font="halston 10 underline", fg='blue')
label6.grid(row=6, column=0, padx=5)
label7 = Label(frame1, text='LinkedIn ID : https://www.linkedin.com/in/subhadipml/', font="halston 10 underline", fg='blue')
label7.grid(row=7, column=0, padx=5)

#---End : All information about the developer---#

def ticket_booking():
    master.destroy()
    ticket_obj = Ticket()
    ticket_obj.hello()
button1 = Button(frame1, text='BOOK Ticket', command=ticket_booking)
button1.grid(row=8, columnspan=4, ipadx=20)


master.mainloop()
