from tkinter import *
from tkinter import messagebox

from excelCreation.helpers import createDataForExcel


## FUNCTION THAT CREATES THE GUI ##
## FROM THE GUI, THE APP RECEIVES THE DATA ##

def createForm(ws): 

    def closeWindow(): 
        ws.destroy() 

    def selection():
        tariffChoice = tariffVar.get()
        if tariffChoice == 1:
            tariffName = 'Privato'
        elif tariffChoice == 2:
            tariffName = 'SSN'
        return tariffName

    def submit():
        try:
            idE = idExam.get()
            name = nameExam.get()
            price = fullPrice.get() 
            tariffName = selection()
            messagebox.showinfo('TariffFileCreation', f'You are creating the Excel for the following data: {idE} {name} {price} , for the following tariff {tariffName}.')
            #Close the main window
            closeWindow()
            createDataForExcel(idE, name, int(price), tariffName)
            return messagebox.showinfo('TariffFileCreation', 'The file has been created.')
        except Exception as ep:
            return messagebox.showwarning('PythonGuides', 'Please provide valid input')


    frame1 = Label(ws, bg='#dddddd')
    frame1.pack()
    frame2 = LabelFrame(frame1, text='Tariff', padx=30, pady=10)

    tariffVar =IntVar()
    cb = IntVar()
    
    Label(frame1, text='Exam ID').grid(row=0, column=0, padx=5, pady=5)
    Label(frame1, text='Exam Name').grid(row=1, column=0, padx=5, pady=5)
    Label(frame1, text='Full Price').grid(row=2, column=0, padx=5, pady=5)
    Radiobutton(frame2, text='Private Tariff', variable=tariffVar, value=1,command=selection).pack()
    Radiobutton(frame2, text='SSN Tariff', variable=tariffVar, value=2,command=selection).pack(anchor=W)
    idExam = Entry(frame1)
    idExam.grid(row=0, column=2)
    nameExam = Entry(frame1)
    nameExam.grid(row=1, column=2)
    fullPrice = Entry(frame1)
    fullPrice.grid(row=2, column=2)
    frame2.grid(row=3, columnspan=3,padx=30)
    # Checkbutton(frame1, text='Accept the terms & conditions', variable=cb, onvalue=1, offvalue=0,command=termsCheck).grid(row=4, columnspan=4, pady=5)
    submit_btn = Button(frame1, text="Submit", command=submit, padx=50, pady=5)
    submit_btn.grid(row=5, columnspan=4, pady=2)

    ws.mainloop()

    

